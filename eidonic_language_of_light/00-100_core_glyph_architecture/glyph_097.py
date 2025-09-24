# glyph_097.py — Anchor Code Inverter
# -----------------------------------------------------------------------------
# ID:            097
# Pack:          Pack 001 (000–100)
# Name:          Anchor Code Inverter
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_097(code: str) -> str:
    """
    Anchor Code Inverter — invert bits and mirror delimiters.

    Overview
    --------
    Flips '0'↔'1' and swaps `<>()[]` with their mirrors while reversing the string.

    Parameters
    ----------
    code : str

    Returns
    -------
    str
        Inverted anchor code.

    Examples
    --------
    >>> glyph_097("01<ab>")
    "<ba>10"
    """
    flip = {"0": "1", "1": "0", "<": ">", ">": "<", "(": ")", ")": "(", "[": "]", "]": "["}
    return "".join(flip.get(ch, ch) for ch in reversed(code))
