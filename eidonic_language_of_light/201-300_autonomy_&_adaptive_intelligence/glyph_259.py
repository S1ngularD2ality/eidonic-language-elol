# glyph_259.py — Dimensional Core Reconstructor
# -----------------------------------------------------------------------------
# ID:            259
# Pack:          Pack 003 (201–300)
# Name:          Dimensional Core Reconstructor
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_259(rows: Sequence[Sequence[float]]) -> List[List[float]]:
    """
    Dimensional Core Reconstructor — rebuild square matrix from row stripes.

    Overview
    --------
    If rows form an m×m square when concatenated, reshape into matrix; else best effort.

    Parameters
    ----------
    rows : Sequence[Sequence[float]]

    Returns
    -------
    List[List[float]]
        Reconstructed matrix (square when possible, else rectangular pass-through).

    Examples
    --------
    >>> glyph_259([[1,2],[3,4]])
    [[1.0, 2.0], [3.0, 4.0]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    flat = [float(v) for r in rows for v in r]
    n = int(len(flat) ** 0.5)
    if n * n != len(flat) or n == 0:
        return [[float(v) for v in r] for r in rows]
    return [flat[i*n:(i+1)*n] for i in range(n)]
