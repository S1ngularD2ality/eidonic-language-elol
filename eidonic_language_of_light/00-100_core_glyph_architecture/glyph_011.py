# glyph_011.py — Inner Mirror Sequencer
# -----------------------------------------------------------------------------
# ID:            011
# Pack:          Pack 001 (000–100)
# Name:          Inner Mirror Sequencer
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

def glyph_011(seq: Sequence[float]) -> List[float]:
    """
    Inner Mirror Sequencer — interleave a sequence with its reverse.

    Overview
    --------
    Emits [x0, xn-1, x1, xn-2, …], preserving length×1 (paired until exhausted).

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    List[float]
        Interleaved mirror sequence.

    Examples
    --------
    >>> glyph_011([1,2,3,4])
    [1.0, 4.0, 2.0, 3.0]
    """
    x = [float(v) for v in seq]
    n = len(x)
    out: List[float] = []
    for i in range((n + 1)//2):
        out.append(x[i])
        if n-1-i != i:
            out.append(x[n-1-i])
    return out
