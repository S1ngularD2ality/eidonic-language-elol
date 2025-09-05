# glyph_988 – ANTI_SIDECHANNEL_DELAY_SCHED
"""
Anti-Sidechannel Delay Scheduler

Adds random jitter and constant-time padding to operations to reduce timing leaks.
Use sparingly; adds latency.

APIs:
- pad_call(fn, min_ms=2, max_ms=7) -> (result, elapsed_ms)
"""

import time, random

def pad_call(fn, min_ms: int = 2, max_ms: int = 7):
    start = time.perf_counter()
    res = fn()
    target = random.uniform(min_ms/1000.0, max_ms/1000.0)
    while (time.perf_counter() - start) < target:
        pass
    elapsed_ms = (time.perf_counter() - start) * 1000.0
    return res, elapsed_ms
