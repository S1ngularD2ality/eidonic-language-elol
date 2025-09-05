# glyph_983 – KEY_USAGE_ANOMALY
"""
Key Usage Anomaly Detector

Learns baseline stats for per-key operations (rate, size, endpoints) and
flags deviations (possible exfiltration / misuse).

APIs:
- class KeyUsageModel().observe(key_id, size, endpoint) -> None
- .score(key_id, size, endpoint) -> float  (higher = more anomalous)
"""

from collections import defaultdict

class KeyUsageModel:
    def __init__(self):
        self.count = defaultdict(int)
        self.bytes = defaultdict(int)
        self.endpoints = defaultdict(set)

    def observe(self, key_id: str, size: int, endpoint: str):
        self.count[key_id] += 1
        self.bytes[key_id] += size
        self.endpoints[key_id].add(endpoint)

    def score(self, key_id: str, size: int, endpoint: str) -> float:
        c = self.count.get(key_id, 0) or 1
        b = self.bytes.get(key_id, 0) or 1
        ep_unique = len(self.endpoints.get(key_id, set())) or 1
        # simple deviation heuristic
        rate_term = 1.0 / (c ** 0.5)
        size_term = size / (b / c)
        ep_term = 1.0 if endpoint in self.endpoints.get(key_id, set()) else 2.0
        return rate_term + 0.1 * size_term + ep_term
