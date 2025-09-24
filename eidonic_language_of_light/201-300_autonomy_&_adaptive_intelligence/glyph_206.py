# glyph_206.py — Symbolic Field Amplifier
# -----------------------------------------------------------------------------
# ID:            206
# Pack:          Pack 003 (201–300)
# Name:          Symbolic Field Amplifier
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

def glyph_206(field: Sequence[Sequence[float]], *, gain: float = 1.2) -> List[List[float]]:
    """
    Symbolic Field Amplifier — multiply a 2D field by a scalar gain.

    Overview
    --------
    Scales all values uniformly, preserving shape and relative structure.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
        2D array-like of numbers.
    gain : float, optional (default: 1.2)
        Scalar multiplier.

    Returns
    -------
    List[List[float]]
        Amplified field.

    Examples
    --------
    >>> glyph_206([[1,2],[3,4]], gain=2.0)
    [[2.0, 4.0], [6.0, 8.0]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H·W)
    """
    g = float(gain)
    return [[float(v) * g for v in row] for row in field]
