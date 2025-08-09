# glyph_977 – RATE_LIMIT_SLIDING_WINDOW
"""
Sliding-Window Rate Limiter

Counts requests within a moving time window, independent of bucket edges.

APIs:
- class SlidingWindow(window_s:int, limit:int).allow(now:float)->bool
"""

from collections import deque

class SlidingWindow:
    def __init__(self, window_s: float, limit: int):
        self.w = window_s
        self.lim = limit
        self.q = deque()

    def allow(self, now: float) -> bool:
        self._gc(now)
        if len(self.q) < self.lim:
            self.q.append(now)
            return True
        return False

    def _gc(self, now: float):
        while self.q and now - self.q[0] > self.w:
            self.q.popleft()
