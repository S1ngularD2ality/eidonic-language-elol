# glyph_107.py — Anchor Field Realigner
# -----------------------------------------------------------------------------
# ID:            107
# Pack:          Pack 002 (101–200)
# Name:          Anchor Field Realigner
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_107(field: Sequence[Sequence[float]]) -> Tuple[List[List[float]], float, float]:
    """
    Anchor Field Realigner — zero-center and scale a 2D field.

    Overview
    --------
    Subtract global mean and divide by global std (fallback 1). Returns (field, mean, std).

    Parameters
    ----------
    field : Sequence[Sequence[float]]

    Returns
    -------
    (List[List[float]], float, float)
        (normalized_field, mean, std)

    Examples
    --------
    >>> glyph_107([[1,2],[3,4]])[1:]
    (2.5, 1.118033988749895)

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H·W)
    """
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]:
        return [], 0.0, 1.0
    vals = [v for r in A for v in r]
    m = sum(vals)/len(vals)
    var = sum((v-m)**2 for v in vals)/len(vals)
    s = (var**0.5) or 1.0
    return [[(v-m)/s for v in r] for r in A], m, s
