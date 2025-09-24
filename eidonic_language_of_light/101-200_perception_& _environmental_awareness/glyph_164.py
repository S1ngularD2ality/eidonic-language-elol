# glyph_164.py — Lightflow Mirror Extractor
# -----------------------------------------------------------------------------
# ID:            164
# Pack:          Pack 002 (101–200)
# Name:          Lightflow Mirror Extractor
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_164(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Lightflow Mirror Extractor — split into symmetric and antisymmetric parts.

    Overview
    --------
    For i from 0..n-1, define j = n-1-i. Outputs:
      sym[i] = (x[i] + x[j])/2
      anti[i] = (x[i] - x[j])/2
    Sym is mirror-even; anti is mirror-odd.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (symmetric_component, antisymmetric_component)

    Examples
    --------
    >>> glyph_164([1,2,3,4])
    ([2.5, 2.5, 2.5, 2.5], [-1.5, -0.5, 0.5, 1.5])
    """
    x = [float(v) for v in seq]
    n = len(x)
    sym = [0.0]*n
    anti = [0.0]*n
    for i in range(n):
        j = n-1-i
        sym[i] = 0.5*(x[i] + x[j])
        anti[i] = 0.5*(x[i] - x[j])
    return sym, anti
