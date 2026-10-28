import copy
import datetime as dt
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import devices
import validate as v

NOW = dt.datetime(2026, 10, 27, 12, tzinfo=dt.timezone.utc)

class DeviceTests(unittest.TestCase):
    def setUp(self):
        self.models, _, _ = devices.load_registry(ROOT)
        self.model = copy.deepcopy(self.models[0])
        self.profile = json.loads((ROOT/'schemas/device-profile.example.json').read_text())
        self.profile.update(id='phone-os-a', device_id=self.model['id'], hardware='exact phone variant', os_build='OS build A')
        self.profile['configuration']['model_identifier'] = 'test-identifier'

    def record(self, **changes):
        e = dict(id='run-one', profile=self.profile['id'], capability='display', kind='physical', status='verified',
                 revision='a'*40, hardware='exact phone variant', os_build='OS build A', tested_at='2026-10-26T12:00:00Z',
                 expires_at='2026-10-28T12:00:00Z', scenario='Synthetic test only', provider_version=None,
                 operator='tester', reviewer='reviewer', procedure=['Perform one reproducible check'], expected='A map appears',
                 observed='A map appeared', artifacts=[dict(url='https://example.org/proof',sha256='b'*64,description='Synthetic fixture')],
                 limitations=['Unit fixture only'], record_path='evidence/records/run-one.json')
        e.update(changes)
        return e

    def test_empty_history_stays_empty_and_not_a_failure(self):
        result = devices.search(self.models, [], [], 'iPhone 13', NOW)
        self.assertEqual(result['exact_matches'], ['apple-iphone-13'])
        self.assertEqual(result['matches'][0]['observation_count'], 0)
        self.assertEqual(result['matches'][0]['configurations'], [])

    def test_device_not_yet_in_manifest_is_not_unsupported(self):
        result = devices.search(self.models, [], [], 'a new device from next year', NOW)
        self.assertEqual(result['matches'], [])
        self.assertIn('support elsewhere is unknown', result['interpretation'])

    def test_new_model_requires_only_data(self):
        new = copy.deepcopy(self.model)
        new.update(id='new-vendor-one', model='A completely new model', manufacturer='A new vendor', aliases=['special handset'])
        result = devices.search([new], [], [], 'special handset', NOW)
        self.assertEqual(result['exact_matches'], ['new-vendor-one'])

    def test_model_identifier_search_separates_screen_variants(self):
        result = devices.search(self.models, [], [], 'Mac17,3', NOW)
        self.assertEqual(result['match_count'], 1)
        self.assertEqual(result['matches'][0]['device']['model'], 'MacBook Air 13-inch M5')

    def test_different_model_and_os_do_not_inherit_results(self):
        other = copy.deepcopy(self.profile)
        other.update(id='phone-os-b', os_build='OS build B')
        result = devices.search(self.models, [self.profile, other], [self.record()], 'iPhone 13', NOW)
        profiles = result['matches'][0]['configurations']
        self.assertEqual([len(p['observations']) for p in profiles], [1, 0])
        unrelated = devices.search(self.models, [self.profile], [self.record()], 'iPhone 14', NOW)
        self.assertEqual(unrelated['matches'][0]['observation_count'], 0)

    def test_failures_revisions_and_evidence_kinds_all_survive(self):
        records = [self.record(), self.record(id='later-failure',revision='c'*40,status='failed'),
                   self.record(id='source-report',kind='source',status='observed')]
        result = devices.search(self.models, [self.profile], records, 'iPhone 13', NOW)
        observations = result['matches'][0]['configurations'][0]['observations']
        self.assertEqual([e['id'] for e in observations], ['run-one','later-failure','source-report'])
        self.assertEqual([e['state_at_query'] for e in observations], ['verified','failed','observed'])

    def test_expiry_is_timezone_aware_and_exact(self):
        self.assertEqual(devices.evidence_state(self.record(expires_at='2026-10-27T05:00:00-07:00'), NOW), 'stale')
        self.assertEqual(devices.evidence_state(self.record(expires_at='2026-10-27T12:00:01Z'), NOW), 'verified')

    def test_placeholder_cannot_receive_a_configuration(self):
        future = next(d for d in self.models if d['identity']=='placeholder')
        self.profile.update(device_id=future['id'],family=future['family'])
        with self.assertRaisesRegex(v.Invalid, 'placeholder'):
            v.validate_devices({future['id']:future}, {'test':self.profile})

    def test_profile_rejects_wrong_known_model_identifier(self):
        mac = next(d for d in self.models if d['model_identifiers'])
        self.profile.update(device_id=mac['id'],family=mac['family'])
        with self.assertRaisesRegex(v.Invalid, 'identifier differs'):
            v.validate_devices({mac['id']:mac}, {'test':self.profile})

    def test_physical_observation_requires_matching_configuration(self):
        for change in ({'os_build':'another OS'}, {'hardware':'another phone'}, {'device_id':None}):
            p = dict(self.profile, **change)
            with self.subTest(change=change), self.assertRaises(v.Invalid):
                v.validate_evidence(self.record(status='observed'), {p['id']:p}, {'display':{}}, NOW)

    def test_verified_evidence_requires_identifier(self):
        self.profile['configuration']['model_identifier'] = None
        with self.assertRaises(v.Invalid):
            v.validate_evidence(self.record(), {self.profile['id']:self.profile}, {'display':{}}, NOW)

    def test_unknown_specs_remain_null(self):
        v.validate_devices({self.model['id']:self.model}, {self.profile['id']:self.profile})
        self.assertIsNone(self.profile['configuration']['ram_gib'])
        self.profile['configuration']['ram_gib'] = 0
        with self.assertRaises(v.Invalid):
            v.validate_devices({self.model['id']:self.model}, {self.profile['id']:self.profile})

    def test_html_escapes_device_names_and_retains_observations(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/'data').mkdir();(root/'evidence/records').mkdir(parents=True)
            self.model['model']='<script>alert("untrusted")</script>'
            (root/'data/devices.json').write_text(json.dumps([self.model]))
            (root/'data/platforms.json').write_text(json.dumps([self.profile]))
            (root/'evidence/records/run-one.json').write_text(json.dumps(self.record()))
            page=devices.render_page(root, NOW)
            self.assertIn('&lt;script&gt;',page)
            self.assertNotIn('<script>alert(',page)
            self.assertIn('run-one.json',page)
            self.assertIn('OS build A',page)
            self.assertIn('data-expires=',page)

if __name__=='__main__': unittest.main()
