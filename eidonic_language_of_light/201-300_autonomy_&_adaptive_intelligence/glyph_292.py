# glyph_292.py — Anchor Resonance Binder
# -----------------------------------------------------------------------------
# ID:            292
# Pack:          Pack 003 (201–300)
# Name:          Anchor Resonance Binder
# Class:         combinator
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple

def glyph_292(a: Sequence[float], b: Sequence[float]) -> Tuple[list[float], list[float]]:
    """
    Anchor Resonance Binder — equalize RMS between two streams.

    Overview
    --------
    Scales A and B to share the same RMS (the mean of original RMS values).

    Parameters
    ----------
    a, b : Sequence[float]

    Returns
    -------
    (list[float], list[float])
        (a_scaled, b_scaled)

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    def rms(x):
        x = [float(v) for v in x]
        return (sum(v*v for v in x)/len(x))**0.5 if x else 0.0
    ra, rb = rms(a), rms(b)
    target = (ra + rb)/2 if (ra>0 and rb>0) else (ra or rb or 1.0)
    sa = target/(ra or 1.0); sb = target/(rb or 1.0)
    return [sa*float(v) for v in a], [sb*float(v) for v in b]
