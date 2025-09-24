# glyph_212.py — Polarity Flame Transposer
# -----------------------------------------------------------------------------
# ID:            212
# Pack:          Pack 003 (201–300)
# Name:          Polarity Flame Transposer
# Class:         transform
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_212(x: float, *, offset: float = 0.0, scale: float = 1.0) -> float:
    """
    Polarity Flame Transposer — affine transform y = scale * (x + offset).

    Overview
    --------
    Deterministic amplitude/polarity shift.

    Parameters
    ----------
    x : float
    offset : float, optional (default: 0.0)
    scale : float, optional (default: 1.0)

    Returns
    -------
    float
        Transposed value.

    Examples
    --------
    >>> glyph_212(2.0, offset=-1.0, scale=3.0)
    3.0

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return float(scale) * (float(x) + float(offset))
