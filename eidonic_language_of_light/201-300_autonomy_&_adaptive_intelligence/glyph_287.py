# glyph_287.py — Subconscious Flame Refiner
# -----------------------------------------------------------------------------
# ID:            287
# Pack:          Pack 003 (201–300)
# Name:          Subconscious Flame Refiner
# Class:         transform
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_287(x: float, *, gamma: float = 0.6) -> float:
    """
    Subconscious Flame Refiner — signed power compression.

    Overview
    --------
    y = sign(x) * |x|^gamma, with gamma∈(0,1].

    Parameters
    ----------
    x : float
    gamma : float, optional (default: 0.6)

    Returns
    -------
    float
        Refined value.

    Exceptions
    ----------
    - ValueError : if `gamma <= 0`.

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if gamma <= 0:
        raise ValueError("gamma must be > 0")
    return (1.0 if x >= 0 else -1.0) * (abs(float(x)) ** float(gamma))
