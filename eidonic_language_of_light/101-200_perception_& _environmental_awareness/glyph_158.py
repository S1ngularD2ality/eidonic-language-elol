# glyph_158.py — Harmonic Gate Reshaper
# -----------------------------------------------------------------------------
# ID:            158
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Gate Reshaper
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_158(x: float, *, gamma: float = 0.5) -> float:
    """
    Harmonic Gate Reshaper — signed power-law compression.

    Overview
    --------
    y = sign(x) * |x|^gamma with 0 < gamma <= 1.

    Parameters
    ----------
    x : float
    gamma : float, optional (default: 0.5)

    Returns
    -------
    float
        Reshaped value.

    Examples
    --------
    >>> glyph_158(9.0, gamma=0.5)
    3.0

    Exceptions
    ----------
    - ValueError : if gamma <= 0.
    """
    if gamma <= 0:
        raise ValueError("gamma must be > 0")
    s = -1.0 if x < 0 else (1.0 if x > 0 else 0.0)
    return s * (abs(float(x)) ** float(gamma))
