# Location

Location is a measurement with provenance. Coordinates alone are insufficient.

Represent unavailable, permission-denied, acquiring, fix, stale and error as distinct states. A fix carries coordinates, source/provider, observed_at (nullable), received_at, horizontal_accuracy_m (nullable), accuracy semantics/confidence level (nullable), optional heading/speed and provenance. Manual start is a chosen point, not a GPS fix.

Missing source time stays unknown, never now. Unknown accuracy stays null, never zero or an invented radius. A provider reporting zero with unknown semantics cannot establish perfect accuracy. Preserve units/coordinate system; reject non-finite/out-of-range input and oversized payloads.

Freshness comes from source time. Receipt time measures transport; it cannot prove fix age. Handle clock skew, reordering, provider switching and future timestamps explicitly. Show age/uncertainty; road snapping must not disguise stale data.

Required cases: unasked/denied/revoked/coarse/precise permission, provider absent, no indoor fix, stale/reordered/future events, absent accuracy, source switch, sleep/resume, no network, lost-fix and reacquisition. Manual planning remains useful.

Linux needs provider, GeoClue and an authorization path for the app identity. Installing GeoClue does not create GPS. Android needs native permission/foreground-service lifecycle. A Linux guest needs an explicit host bridge.

Synthetic replay proves state handling; service tests prove adapter behavior; emulators prove emulated input. Outdoor navigation needs physical evidence. Receiver scatter around its own mean measures repeatability, not absolute accuracy.

No raw home routes in public evidence. Prefer synthetic fixtures/public landmarks with consent; trim sensitive traces. Removing endpoints alone may not anonymize a route.
