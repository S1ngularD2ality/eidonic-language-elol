# glyph_042.py — Aura Phase Switcher
# -----------------------------------------------------------------------------
# ID:            042
# Pack:          Pack 001 (000–100)
# Name:          Aura Phase Switcher
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_042(seq: Sequence[float], *, shift: int) -> List[float]:
    """
    Aura Phase Switcher — circularly shift a sequence by `shift` steps.

    Overview
    --------
    Performs modular rotation on `seq`. Positive `shift` moves elements forward (to
    higher indices), wrapping around. Preserves length and type (floats).

    Parameters
    ----------
    seq : Sequence[float]
        Input samples.
    shift : int
        Number of positions to rotate; may be negative.

    Returns
    -------
    List[float]
        Rotated sequence.

    Examples
    --------
    >>> glyph_042([1,2,3,4], shift=1)
    [4,1,2,3]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    n = len(seq)
    if n == 0:
        return []
    k = shift % n
    if k == 0:
        return [float(v) for v in seq]
    return [float(seq[(i - k) % n]) for i in range(n)]
