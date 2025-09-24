# glyph_180.py — Symbolic Core Dissolver
# -----------------------------------------------------------------------------
# ID:            180
# Pack:          Pack 002 (101–200)
# Name:          Symbolic Core Dissolver
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_180(text: str, *, remove: str) -> str:
    """
    Symbolic Core Dissolver — strip a set of symbols from text.

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
        Dissolved text without the specified characters.

    Examples
    --------
    >>> glyph_180("a-b_c", remove="-_")
    'abc'
    """
    drop = {ch for ch in remove}
    return "".join(ch for ch in text if ch not in drop)
