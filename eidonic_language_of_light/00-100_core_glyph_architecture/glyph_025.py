# glyph_025.py — Mirror Lens Realigner
# -----------------------------------------------------------------------------
# ID:            025
# Pack:          Pack 001 (000–100)
# Name:          Mirror Lens Realigner
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_025(text: str) -> str:
    """
    Mirror Lens Realigner — reverse the text and swap common mirror delimiters.

    Overview
    --------
    Produces reversed text, flipping <->, () and [] pairs while leaving other
    characters as-is.

    Parameters
    ----------
    text : str

    Returns
    -------
    str
        Realigned mirror string.

    Examples
    --------
    >>> glyph_025("<(ab)>")
    "<[ba]>"
    """
    mirror = {"<": ">", ">": "<", "(": ")", ")": "(", "[": "]", "]": "["}
    out = []
    for ch in reversed(text):
        out.append(mirror.get(ch, ch))
    return "".join(out)
