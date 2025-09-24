# glyph_294.py — Dream Sequence Disruptor
# -----------------------------------------------------------------------------
# ID:            294
# Pack:          Pack 003 (201–300)
# Name:          Dream Sequence Disruptor
# Class:         filter
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_294(seq: Sequence[float], *, stride: int = 2) -> List[float]:
    """
    Dream Sequence Disruptor — zero every `stride`-th element (1-based).

    Overview
    --------
    Deterministically introduces silence/void beats.

    Parameters
    ----------
    seq : Sequence[float]
    stride : int, optional (default: 2)

    Returns
    -------
    List[float]
        Disrupted sequence.

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    s = max(1, int(stride))
    out=[]
    for i, v in enumerate(seq, start=1):
        out.append(0.0 if (i % s == 0) else float(v))
    return out
