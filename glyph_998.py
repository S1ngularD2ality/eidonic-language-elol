# glyph_998 – DEADMAN_SWITCH
"""
Dead Man's Switch

Triggers a predefined action if heartbeats stop before deadline.

APIs:
- class Deadman(timeout_s: float, trigger: callable).beat()->None; check(now: float)->bool
"""

import time
from typing import Callable

class Deadman:
    def __init__(self, timeout_s: float, trigger: Callable[[], None]):
        self.to = timeout_s
        self.trigger = trigger
        self.last = time.time()

    def beat(self):
        self.last = time.time()

    def check(self, now: float | None = None) -> bool:
        t = now if now is not None else time.time()
        if (t - self.last) > self.to:
            self.trigger()
            return True
        return False
