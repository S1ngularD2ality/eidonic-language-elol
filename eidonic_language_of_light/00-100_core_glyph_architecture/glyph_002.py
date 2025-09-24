# glyph_002.py — Mirror Core Rewriter
# -----------------------------------------------------------------------------
# ID:            002
# Pack:          Pack 001 (000–100)
# Name:          Mirror Core Rewriter
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, List

def glyph_002(text: str, pairs: Mapping[str, str]) -> str:
    """
    Mirror Core Rewriter — perform an involutive, symmetric rewrite on text.

    Overview
    --------
    Enforces symmetry on `pairs` (if a→b exists, ensure b→a). Applies replacements
    longest-key-first, then falls back to single-character mirroring.

    Parameters
    ----------
    text : str
        Input text.
    pairs : Mapping[str, str]
        Token/character mapping; asymmetric input is symmetrized.

    Returns
    -------
    str
        Rewritten text.

    Examples
    --------
    >>> glyph_002("<ab>", {"<": ">", ">": "<", "ab":"ba"})
    '><ba<'
    """
    sym = dict(pairs)
    for k, v in list(sym.items()):
        if sym.get(v) != k:
            sym[v] = k
    keys = sorted(sym.keys(), key=len, reverse=True)
    out: List[str] = []
    i = 0
    while i < len(text):
        for k in keys:
            if k and text.startswith(k, i):
                out.append(sym[k]); i += len(k); break
        else:
            ch = text[i]
            out.append(sym.get(ch, ch)); i += 1
    return "".join(out)
