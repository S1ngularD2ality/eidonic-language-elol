# glyph_188.py — Flame Signal Disruptor
# -----------------------------------------------------------------------------
# ID:            188
# Pack:          Pack 002 (101–200)
# Name:          Flame Signal Disruptor
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_188(seq: Sequence[float], *, stride: int = 2) -> List[float]:
    """
    Flame Signal Disruptor — periodic dropout mask.

    Overview
    --------
    Zeros every `stride`-th element (1-based), preserving others.

    Parameters
    ----------
    seq : Sequence[float]
    stride : int, optional (default: 2)

    Returns
    -------
    List[float]
        Disrupted sequence.

    Examples
    --------
    >>> glyph_188([1,2,3,4,5], stride=2)
    [1.0, 0.0, 3.0, 0.0, 5.0]
    """
    s = max(1, int(stride))
    out: List[float] = []
    for i, v in enumerate(seq, start=1):
        out.append(0.0 if (i % s == 0) else float(v))
    return out
