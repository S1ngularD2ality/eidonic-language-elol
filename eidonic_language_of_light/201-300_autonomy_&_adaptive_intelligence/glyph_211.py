# glyph_211.py — Harmonic Core Scrambler
# -----------------------------------------------------------------------------
# ID:            211
# Pack:          Pack 003 (201–300)
# Name:          Harmonic Core Scrambler
# Class:         transform
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_211(seq: Sequence[float], *, stride: int = 2) -> List[float]:
    """
    Harmonic Core Scrambler — block-wise reversal with stride.

    Overview
    --------
    Splits into chunks of length `stride` and reverses each chunk in place.

    Parameters
    ----------
    seq : Sequence[float]
    stride : int, optional (default: 2)

    Returns
    -------
    List[float]
        Scrambled sequence.

    Examples
    --------
    >>> glyph_211([0,1,2,3,4], stride=2)
    [1.0, 0.0, 3.0, 2.0, 4.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    s = max(1, int(stride))
    x = [float(v) for v in seq]
    out: List[float] = []
    for i in range(0, len(x), s):
        out += list(reversed(x[i:i+s]))
    return out
