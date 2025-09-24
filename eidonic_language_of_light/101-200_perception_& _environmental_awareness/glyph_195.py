# glyph_195.py — Symbolic Cascade Modulator
# -----------------------------------------------------------------------------
# ID:            195
# Pack:          Pack 002 (101–200)
# Name:          Symbolic Cascade Modulator
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_195(text: str, *, pattern: str = "Aa") -> str:
    """
    Symbolic Cascade Modulator — apply alternating-case modulation.

    Overview
    --------
    Cycles through `pattern` to transform alphabetic characters:
    'A' → uppercase, 'a' → lowercase, other chars copied unchanged.

    Parameters
    ----------
    text : str
    pattern : str, optional (default: "Aa")

    Returns
    -------
    str
        Modulated text.

    Examples
    --------
    >>> glyph_195("mirror", pattern="Aa")
    'MiRrOr'
    """
    if not pattern:
        return text
    out = []
    pi = 0
    for ch in text:
        p = pattern[pi % len(pattern)]
        if ch.isalpha():
            out.append(ch.upper() if p == "A" else ch.lower())
            pi += 1
        else:
            out.append(ch)
    return "".join(out)
