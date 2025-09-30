# glyph_450.py — Redaction Veil
# -----------------------------------------------------------------------------
# ID:            450
# Pack:          Pack 005 (401–500)
# Name:          Redaction Veil
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import re

def glyph_450(text: str, patterns: list[str], *, mask: str = "█") -> str:
    """
    Redaction Veil — redact substrings matching any regex pattern.

    Overview
    --------
    Replaces each match with a run of `mask` characters of equal length.

    Parameters
    ----------
    text     : str
    patterns : list[str]
    mask     : str, optional (default: "█")

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_450("Email a@b.com", [r"[\\w.]+@[\\w.]+"])
    'Email ████████'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n·p)
    - Space : O(n)
    """
    out = text
    for pat in patterns:
        def repl(m): return mask * (m.end() - m.start())
        out = re.sub(pat, repl, out)
    return out
