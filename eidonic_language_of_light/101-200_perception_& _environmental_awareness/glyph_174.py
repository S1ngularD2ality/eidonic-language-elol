# glyph_174.py — Harmonic Channel Inverter
# -----------------------------------------------------------------------------
# ID:            174
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Channel Inverter
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_174(left: Sequence[float], right: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Harmonic Channel Inverter — swap channels and invert one phase.

    Overview
    --------
    Returns (right, -left), a simple L/R inversion often used to test parity.

    Parameters
    ----------
    left  : Sequence[float]
    right : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (new_left, new_right)

    Examples
    --------
    >>> glyph_174([1,2],[3,4])
    ([3.0, 4.0], [-1.0, -2.0])
    """
    L = [float(v) for v in left]
    R = [float(v) for v in right]
    m = min(len(L), len(R))
    return R[:m], [-v for v in L[:m]]
