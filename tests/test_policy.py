import copy
import datetime as dt
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
def module(name):
    s=importlib.util.spec_from_file_location(name,ROOT/"tools"/(name+".py"))
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
v=module("validate");p=module("trusted_policy");render=module("render")
class PolicyTests(unittest.TestCase):
    def evidence(self):
        now=dt.datetime.now(dt.timezone.utc)
        return dict(id="test-only",profile="test",capability="display",kind="physical",status="verified",
                    scenario="Synthetic unit-test record; never shipped as device proof.",revision="a"*40,
                    hardware="test model",os_build="test OS",provider_version=None,operator="operator",
                    reviewer="reviewer",tested_at=now.isoformat(),expires_at=(now+dt.timedelta(days=30)).isoformat(),
                    procedure=["Observe the test fixture"],expected="Expected test result",observed="Observed test result",
                    artifacts=[dict(url="https://example.org/fixture",sha256="b"*64,description="test fixture")],
                    limitations=["Unit test only"])
    def check(self,e):v.validate_evidence(e,{"test":{"hardware":"test model","os_build":"test OS","device_id":"test-device","configuration":{"model_identifier":"test-model-id"}}},{"display":{}})
    def test_family_profile_cannot_be_verified(self):
        with self.assertRaises(v.Invalid):v.validate_evidence(self.evidence(),{"test":{"hardware":None,"os_build":None}},{"display":{}})
    def test_complete_physical_record_structure(self):self.check(self.evidence())
    def test_unknown_measurement_cannot_be_verified(self):
        e=self.evidence();e["tested_at"]=None
        with self.assertRaises(v.Invalid):self.check(e)
    def test_replay_cannot_certify_hardware(self):
        e=self.evidence();e["kind"]="replay"
        with self.assertRaises(v.Invalid):self.check(e)
    def test_author_cannot_review_case_insensitively(self):
        e=self.evidence();e["reviewer"]="Operator"
        with self.assertRaises(v.Invalid):self.check(e)
    def test_no_artifact_is_not_proof(self):
        e=self.evidence();e["artifacts"]=[]
        with self.assertRaises(v.Invalid):self.check(e)
    def test_future_test_rejected(self):
        e=self.evidence();e["tested_at"]=(dt.datetime.now(dt.timezone.utc)+dt.timedelta(days=2)).isoformat()
        with self.assertRaises(v.Invalid):self.check(e)
    def test_unrun_cannot_contain_result(self):
        e=self.evidence();e["status"]="not-tested"
        with self.assertRaises(v.Invalid):self.check(e)
    def test_short_revision_rejected(self):
        e=self.evidence();e["revision"]="abc123"
        with self.assertRaises(v.Invalid):self.check(e)
    def test_path_traversal_and_control_rejected(self):
        for x in ("../secret","/etc/passwd","a/../b","a\\b","a\nb",".git/config"):
            with self.subTest(x=x),self.assertRaises(v.Invalid):v.safe_path(x)
    def test_symlink_tree_rejected(self):
        t=dict(truncated=False,tree=[dict(path="data/x",mode="120000",type="blob",size=1,sha="a"*40)])
        with self.assertRaises(p.v.Invalid):p.tree_entries(t)
    def test_submodule_tree_rejected(self):
        t=dict(truncated=False,tree=[dict(path="vendor",mode="160000",type="commit",sha="a"*40)])
        with self.assertRaises(p.v.Invalid):p.tree_entries(t)
    def test_oversized_or_truncated_tree_rejected(self):
        for t in (dict(truncated=True,tree=[]),dict(truncated=False,tree=[dict(path="x",mode="100644",type="blob",size=v.MAX_FILE+1,sha="a"*40)])):
            with self.assertRaises(p.v.Invalid):p.tree_entries(t)
    def test_incomplete_pr_body_rejected(self):
        with self.assertRaises(p.v.Invalid):p.check_body("Task: DOC-01\n## Purpose\nTODO",{"DOC-01":{}})
    def test_pr_body_is_data(self):
        body="Task: DOC-01\n"+"\n".join("## "+s+"\n"+"This section explains a checked result. "+'$(touch /tmp/never-run)' for s in p.SECTIONS)
        self.assertEqual(p.check_body(body,{"DOC-01":{}}),"DOC-01")
    def test_duplicate_json_key_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/"x.json";f.write_text('{"cost":null,"cost":0}')
            with self.assertRaises(v.Invalid):v.read_json(f)
    def test_unknown_cost_is_not_zero(self):
        r=json.loads((ROOT/"schemas/run-receipt.example.json").read_text())
        r["cost"]=0
        with self.assertRaises(v.Invalid):v.validate_receipt(r,{"DOC-01":{}})
        r["cost_kind"]="measured";r["currency"]="USD"
        v.validate_receipt(r,{"DOC-01":{}})
    def test_html_escapes_contributor_text(self):
        self.assertEqual(render.h('<script>"x"</script>'),'&lt;script&gt;&quot;x&quot;&lt;/script&gt;')
    def test_later_failure_supersedes_pass(self):
        first=self.evidence();first["profile"]="test";first["tested_at"]="2026-01-01T00:00:00Z"
        second=copy.deepcopy(first);second["status"]="failed";second["tested_at"]="2026-02-01T00:00:00Z"
        self.assertEqual(render.cell_status([first,second],"test","display","2026-03-01")[0],"failed")
    def test_expired_verification_is_stale(self):
        e=self.evidence();e["expires_at"]="2025-01-01T00:00:00Z"
        self.assertEqual(render.cell_status([e],"test","display","2026-10-27")[0],"stale")
    def test_no_record_is_not_tested(self):
        self.assertEqual(render.cell_status([],"test","display","2026-10-27"),("not-tested",None))
    def test_duplicate_ids_rejected(self):
        with self.assertRaises(v.Invalid):v.index([{"id":"same"},{"id":"same"}],"fixture")
if __name__=="__main__":unittest.main()
