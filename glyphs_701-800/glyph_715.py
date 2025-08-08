# glyph_715 – CONTEXT_DRIFT_MONITOR
# Detect semantic drift by tracking feature vectors over time.

import math

class glyph_715:
    """
    .update(vec) appends embedding; .drift() returns cosine distance between last and baseline.
    """
    def __init__(self):
        self.baseline = None
        self.latest = None

    def update(self, vec):
        if self.baseline is None:
            self.baseline = list(vec)
        self.latest = list(vec)

    def _cosine(self, a, b):
        dot = sum(x*y for x, y in zip(a, b))
        na = math.sqrt(sum(x*x for x in a))
        nb = math.sqrt(sum(y*y for y in b))
        if na == 0 or nb == 0:
            return 1.0
        return dot / (na * nb)

    def drift(self):
        if self.baseline is None or self.latest is None:
            return 0.0
        return 1.0 - self._cosine(self.baseline, self.latest)
