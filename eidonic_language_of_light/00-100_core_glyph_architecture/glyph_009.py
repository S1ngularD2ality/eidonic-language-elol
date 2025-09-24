# glyph_009.py — Temporal Fractal Imprinter
# -----------------------------------------------------------------------------
# ID:            009
# Pack:          Pack 001 (000–100)
# Name:          Temporal Fractal Imprinter
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

def glyph_009(seq: Sequence[int], *, depth: int) -> List[int]:
    """
    Temporal Fractal Imprinter — recursively echo a motif across time.

    Overview
    --------
    Builds repeated echoes by concatenating progressively offset copies.

    Parameters
    ----------
    seq : Sequence[int]
    depth : int
        Number of echo layers (>= 0).

    Returns
    -------
    List[int]
        Imprinted signal.

    Examples
    --------
    >>> glyph_009([1,0], depth=2)
    [1,0, 1,0, 1,0]

    Exceptions
    ----------
    - ValueError : if `depth < 0`.

    Complexity
    ----------
    - Time  : O(n·depth)
    - Space : O(n·depth)
    """
    if depth < 0:
        raise ValueError("depth must be >= 0")
    out: List[int] = []
    for _ in range(depth or 1):
        out += list(int(v) for v in seq)
    return out
