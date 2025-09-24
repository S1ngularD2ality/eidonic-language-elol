# glyph_058.py — Echo Pulse Translator
# -----------------------------------------------------------------------------
# ID:            058
# Pack:          Pack 001 (000–100)
# Name:          Echo Pulse Translator
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_058(seq: Sequence[float], echoes: Sequence[Tuple[int, float]]) -> List[float]:
    """
    Echo Pulse Translator — add delayed, weighted echoes to a signal.

    Overview
    --------
    For each `(delay, gain)` in `echoes`, add `gain * seq[i]` to index `i+delay` if in range.
    Useful for simple reverbs or causal influence trails.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    echoes : Sequence[Tuple[int, float]]
        List of (delay, gain) pairs.

    Returns
    -------
    List[float]
        Sequence with echoes applied.

    Examples
    --------
    >>> glyph_058([1,0,0,0], echoes=[(1,0.5),(2,0.25)])
    [1.0, 0.5, 0.25, 0.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n · |echoes|)
    - Space : O(n)
    """
    n = len(seq)
    out = [0.0] * n
    for i, v in enumerate(seq):
        out[i] += float(v)
        for d, g in echoes:
            j = i + int(d)
            if 0 <= j < n:
                out[j] += float(v) * float(g)
    return out
