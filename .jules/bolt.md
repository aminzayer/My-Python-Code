## 2024-05-24 - fake_useragent UserAgent() instantiation in loops
**Learning:** `UserAgent()` from `fake_useragent` parses a large JSON file and fetches data on instantiation, taking ~0.6 seconds per call. If done inside a loop (e.g. for creating requests), it creates a huge performance bottleneck.
**Action:** Always instantiate `UserAgent` once outside the loop when making multiple requests, then use `ua.random` inside the loop.
