# Kelowna Transit Investigation

Kelowna is a proposed regional example, not a declared support area. [BC Transit's catalog](https://www.bctransit.com/open-data/) lists these four separate inputs for Kelowna, checked 2026-10-28:

| Input | Catalog URL |
|---|---|
| Static GTFS schedules | https://bct.tmix.se/Tmix.Cap.TdExport.WebApi/gtfs/?operatorIds=47 |
| Service alerts | https://bct.tmix.se/gtfs-realtime/alerts.pb?operatorIds=47 |
| Trip updates | https://bct.tmix.se/gtfs-realtime/tripupdates.pb?operatorIds=47 |
| Vehicle positions | https://bct.tmix.se/gtfs-realtime/vehicleupdates.pb?operatorIds=47 |

Re-resolve the links from the catalog before use. No feed was downloaded, decoded or freshness-tested in this planning change. The [agency terms](https://www.bctransit.com/open-data/terms-of-use/) have conditions and attribution requirements; capture the applicable version and accepted use. Do not label the source CC0 or infer approval from public download access.

## Procedure for the Accepted Run

1. Agree a bounded snapshot and resource cap. Record the final URLs, retrieval time, hashes, service interval, agency time zone and applicable terms. Keep large inputs out of git.
2. Run the [MobilityData static validator](https://github.com/MobilityData/gtfs-validator) and preserve warnings. Feed validity and itinerary correctness are different findings.
3. Build MOTIS from an inspected pinned revision using an OSM region with enough surrounding network for transfers and boundary-crossing trips. Measure import time and peak disk/RAM before deciding the deployment region.
4. Use the same fixed-clock fixtures for MOTIS and any justified OTP comparison: direct ride, transfer, last feasible trip, after-midnight service, weekend/exception day and no service.
5. Join realtime with the right feed/trip/service context. Test cancellation, skipped stop, mismatched IDs, out-of-order updates, reconnect, and absent/stale realtime. Expired predictions become an explicitly labeled schedule fallback. Vehicle positions do not establish arrival accuracy.
6. Keep wheelchair access, fares and absent fields unknown. Check selected public-stop journeys against agency information and independent observations. Google agreement alone is not an acceptance oracle.
7. Record request destinations, refresh load and failure behavior. UI work starts with itineraries, alternatives, walking legs and scheduled/realtime labels. A usable result still needs the platform/security and independent review appropriate to its claim.

Static/realtime implementation belongs to TRANSIT-02 — Scheduled regional transit and TRANSIT-03 — Freshness-aware realtime. Neither depends on phone navigation. Production publication still needs an accountable operator and accepted data rights. CI uses fixtures, not repeated public endpoint requests.
