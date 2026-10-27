# Providers and costs

Donated agent runs pay for development compute, not tiles, geocoding, routing or pack distribution. No provider, operator, production bill or forecast is selected. These values are unknown.

DATA-01 compares a complete region workflow. For each service/pack, record: operator, dataset/code/style/font licenses, checked source URL, attribution, cache/prefetch/offline/distribution rights, coverage/language, freshness, usage units, quotas, price/currency, user/request assumptions, estimate/method, hard cap, outage/migration plan and privacy disclosure. MIT here does not relicense OpenStreetMap data. Review actual ODbL/distribution obligations and seek qualified advice when needed.

## Public services
The standard OSM tile endpoint prohibits bulk prefetch/offline packs and requires attribution, identifying requests and compliant caching. It is not a free pack backend.

Public Nominatim has a maximum aggregate application rate of one request/second, prohibits autocomplete and requires a deliberate accountable operator decision. Do not make it a generic default across agents. Use fixtures in CI; no public-service load tests.

https://operations.osmfoundation.org/policies/tiles/
https://operations.osmfoundation.org/policies/nominatim/

## Packs
Record bounds, coverage, version, compatible engine, terms, byte size, update date, hash and trusted origin. A checksum detects corruption, not publisher identity; add reviewed signatures/provenance. Test disk-full, interrupted download, archive traversal, decompression limits, atomic update, rollback and expiry. Display/search/routing coverage are separate.

Estimate operating costs from declared active users × operations × billed unit plus storage/egress/update work. Separate measurements, assumptions and unknowns. Enforce caps and failure UI before paid traffic. No contributor may bind the project to a subscription.
