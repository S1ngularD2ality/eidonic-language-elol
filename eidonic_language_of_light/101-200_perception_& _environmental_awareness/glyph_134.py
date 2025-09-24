# glyph_134.py — Mirror Cascade Loopbinder
# -----------------------------------------------------------------------------
# ID:            134
# Pack:          Pack 002 (101–200)
# Name:          Mirror Cascade Loopbinder
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_134(seq: Sequence[int], *, loops: int = 1) -> bool:
    """
    Mirror Cascade Loopbinder — verify a loop closes with mirror symmetry.

    Overview
    --------
    Returns True iff concatenating `loops` copies yields palindromic endpoints:
    first == last after loop closure.

    Parameters
    ----------
    seq : Sequence[int]
    loops : int, optional (default: 1)

    Returns
    -------
    bool
        Whether loop is mirror-closed.
    """
    if loops < 1 or not seq:
        return False
    s = list(seq) * loops
    return s[0] == s[-1]
