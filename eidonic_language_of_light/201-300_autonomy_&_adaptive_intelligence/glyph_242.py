# glyph_242.py — Symbol Gate Refiner
# -----------------------------------------------------------------------------
# ID:            242
# Pack:          Pack 003 (201–300)
# Name:          Symbol Gate Refiner
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping

def glyph_242(text: str, *, gate: Mapping[str, str]) -> str:
    """
    Symbol Gate Refiner — whitelist + normalize characters/tokens.

    Overview
    --------
    Keeps only keys present in `gate`, mapping to canonical forms; drops others.

    Parameters
    ----------
    text : str
    gate : Mapping[str, str]

    Returns
    -------
    str
        Refined text.

    Examples
    --------
    >>> glyph_242("A-α-B", gate={"A":"A","B":"B"})
    'AB'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(len(text))
    - Space : O(len(text))
    """
    out = []
    for ch in text:
        if ch in gate:
            out.append(gate[ch])
    return "".join(out)
