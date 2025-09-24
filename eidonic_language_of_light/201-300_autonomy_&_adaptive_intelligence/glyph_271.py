# glyph_271.py — Intention Phase Refiner
# -----------------------------------------------------------------------------
# ID:            271
# Pack:          Pack 003 (201–300)
# Original Name: Intention Phase Refiner
# Manifest Name: Intention Phase Refiner
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_271(seq: Sequence[float], *, target_rms: float = 1.0) -> List[float]:
    """
    Intention Phase Refiner — RMS normalize to a target magnitude.

    Overview
    --------
    Scales sequence so RMS equals `target_rms` (if non-zero input).

    Parameters
    ----------
    seq : Sequence[float]
    target_rms : float, optional (default: 1.0)

    Returns
    -------
    List[float]
        Refined (normalized) sequence.

    Examples
    --------
    >>> glyph_271([1, -1, 1, -1], target_rms=2.0)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    if not x:
        return []
    rms = (sum(v*v for v in x)/len(x))**0.5
    if rms == 0:
        return [0.0]*len(x)
    g = float(target_rms)/rms
    return [g*v for v in x]
