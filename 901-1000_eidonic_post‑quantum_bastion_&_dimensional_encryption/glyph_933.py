# glyph_933 – TOKEN_BUCKET_SHIELD
"""
Token Bucket + Exponential Backoff

Rate-limits sensitive endpoints and penalizes bursts to resist automated probing.
"""

import time
from dataclasses import dataclass

@dataclass
class TokenBucket:
    capacity: int
    refill_per_sec: float
    tokens: float = 0.0
    last: float = time.time()

    def allow(self, cost: float = 1.0) -> bool:
        now = time.time()
        self.tokens = min(self.capacity, self.tokens + (now - self.last)*self.refill_per_sec)
        self.last = now
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False

def backoff(attempt: int, base_ms: int = 100) -> float:
    return (base_ms * (2 ** attempt)) / 1000.0
