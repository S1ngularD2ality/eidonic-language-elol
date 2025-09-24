# glyph_156.py — Symbolic Dream Extender
# -----------------------------------------------------------------------------
# ID:            156
# Pack:          Pack 002 (101–200)
# Name:          Symbolic Dream Extender
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_156(token: str, *, times: int = 3) -> list[str]:
    """
    Symbolic Dream Extender — repeat a token `times` and join.

    Overview
    --------
    Returns token * times (string repetition).

    Parameters
    ----------
    token : str
    times : int, optional (default: 3)

    Returns
    -------
    list[str]
        Single-element list containing the extended token.
    """
    t = max(0, int(times))
    return [token * t]
