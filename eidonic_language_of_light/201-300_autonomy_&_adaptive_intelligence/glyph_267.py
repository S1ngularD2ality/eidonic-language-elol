# glyph_267.py — Quantum Field Deflector
# -----------------------------------------------------------------------------
# ID:            267
# Pack:          Pack 003 (201–300)
# Original Name: Quantum Field Deflector
# Manifest Name: Quantum Field Deflector
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_267(vec: Sequence[float], *, direction: Sequence[float]) -> Tuple[List[float], float]:
    """
    Quantum Field Deflector — project a vector onto a direction.

    Overview
    --------
    Returns (projection of `vec` onto `direction`, scalar gain).

    Parameters
    ----------
    vec : Sequence[float]
    direction : Sequence[float]

    Returns
    -------
    (List[float], float)
        (projected_vector, gain)

    Examples
    --------
    >>> glyph_267([1, 2], direction=[2, 0])
    ([1.0, 0.0], 0.5)

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    v = [float(x) for x in vec]
    d = [float(x) for x in direction]
    if not v or not d:
        return [], 0.0
    dot = sum(a*b for a, b in zip(v, d))
    norm = sum(b*b for b in d) or 1.0
    gain = dot / norm
    proj = [gain * b for b in d]
    return proj, gain
