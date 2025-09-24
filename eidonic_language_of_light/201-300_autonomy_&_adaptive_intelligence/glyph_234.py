# glyph_234.py — Thought Form Patterner
# -----------------------------------------------------------------------------
# ID:            234
# Pack:          Pack 003 (201–300)
# Name:          Thought Form Patterner
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_234(text: str, *, motif: str, times: int = 1) -> str:
    """
    Thought Form Patterner — interleave text with a repeating motif.

    Overview
    --------
    Returns motif.join(chars(text)) repeated `times` between characters.

    Parameters
    ----------
    text : str
    motif : str
    times : int, optional (default: 1)

    Returns
    -------
    str
        Patterned text.
    """
    rep = motif * max(0, int(times))
    return rep.join(list(text))
