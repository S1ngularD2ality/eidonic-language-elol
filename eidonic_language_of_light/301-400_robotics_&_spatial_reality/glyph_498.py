# glyph_498.py — Mirror Channel
# -----------------------------------------------------------------------------
# ID:            498
# Pack:          Pack 005 (401–500)
# Name:          Mirror Channel
# Class:         transformer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_498(text: str) -> str:
    """
    Mirror Channel — reverse string channels between pipes: 'a|b|c' → 'c|b|a'.

    Overview
    --------
    Splits on '|' and rejoins reversed; idempotent for length<=1.

    Parameters
    ----------
    text : str

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_498("east|west|north")
    'north|west|east'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    parts = [p for p in text.split("|")]
    parts.reverse()
    return "|".join(parts)
