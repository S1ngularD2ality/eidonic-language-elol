# glyph_260.py — Spiral Symmetry Dissolver
# -----------------------------------------------------------------------------
# ID:            260
# Pack:          Pack 003 (201–300)
# Name:          Spiral Symmetry Dissolver
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_260(text: str, *, remove: str) -> str:
    """
    Spiral Symmetry Dissolver — strip a set of characters from text.

    Overview
    --------
    Deletes any character appearing in `remove` from `text`. Unicode-safe, order
    preserving, no regex.

    Parameters
    ----------
    text : str
    remove : str

    Returns
    -------
    str
        Dissolved text.

    Examples
    --------
    >>> glyph_260("a-b_c", remove="-_")
    'abc'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(len(text))
    - Space : O(len(text))
    """
    drop = set(remove)
    return "".join(ch for ch in text if ch not in drop)
