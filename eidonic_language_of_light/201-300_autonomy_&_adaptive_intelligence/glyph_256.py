# glyph_256.py — Intention Field Redirector
# -----------------------------------------------------------------------------
# ID:            256
# Pack:          Pack 003 (201–300)
# Name:          Intention Field Redirector
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_256(vec: Sequence[float], *, direction: Sequence[float]) -> Tuple[List[float], float]:
    """
    Intention Field Redirector — project vector onto a direction.

    Overview
    --------
    Returns the projection of `vec` onto `direction` and the scalar gain.

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
    >>> glyph_256([1,2], direction=[2,0])
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
