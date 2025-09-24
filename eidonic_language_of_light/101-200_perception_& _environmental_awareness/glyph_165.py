# glyph_165.py — Dream Core Resequencer
# -----------------------------------------------------------------------------
# ID:            165
# Pack:          Pack 002 (101–200)
# Name:          Dream Core Resequencer
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_165(seq: Sequence[int], order: Sequence[int]) -> List[int]:
    """
    Dream Core Resequencer — reorder chunks by an index permutation.

    Overview
    --------
    Splits `seq` into len(order) equal (or near-equal) chunks; outputs them in the
    order specified by `order` (indices into chunks). Excess tail stays in last chunk.

    Parameters
    ----------
    seq : Sequence[int]
    order : Sequence[int]

    Returns
    -------
    List[int]
        Resequenced stream.

    Examples
    --------
    >>> glyph_165([0,1,2,3,4,5], order=[1,0])
    [3, 4, 5, 0, 1, 2]
    """
    n = len(seq)
    k = max(1, len(order))
    size = (n + k - 1) // k
    chunks = [list(seq[i*size:(i+1)*size]) for i in range(k)]
    out: List[int] = []
    for idx in order:
        if 0 <= idx < k:
            out += chunks[idx]
    return out
