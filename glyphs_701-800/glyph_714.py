# glyph_714 – AUTONOMOUS_TEST_CYCLE
# Continuous sandbox test runner with metrics.

import statistics
import time

class glyph_714:
    """
    .run(tests, rounds) where tests is list of callables -> bool
    Returns summary: pass_rate, avg_duration, failures
    """
    def run(self, tests, rounds=1):
        durations, failures, passes, total = [], 0, 0, 0
        for _ in range(rounds):
            for t in tests:
                start = time.time()
                try:
                    ok = bool(t())
                except Exception:
                    ok = False
                durations.append(time.time() - start)
                failures += 0 if ok else 1
                passes += 1 if ok else 0
                total += 1
        return {
            "pass_rate": passes / max(1, total),
            "avg_duration": statistics.mean(durations) if durations else 0.0,
            "failures": failures,
            "total": total
        }
