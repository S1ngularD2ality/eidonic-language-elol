# glyph_427.py — Scene Narrator
# -----------------------------------------------------------------------------
# ID:            427
# Pack:          Pack 005 (401–500)
# Name:          Scene Narrator
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Sequence

def glyph_427(summary: Mapping[str, int], order: Sequence[str] = ()) -> str:
    """
    Scene Narrator — describe counts per class.

    Overview
    --------
    Emits "name×count" segments ordered by `order` then alphabetically.

    Parameters
    ----------
    summary : Mapping[str,int]
    order   : Sequence[str], optional

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_427({"person":2,"dog":1}, order=["person"])
    'person×2, dog×1'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k log k)
    - Space : O(k)
    """
    keys = list(summary.keys())
    pref = [k for k in order if k in summary]
    rest = sorted(k for k in keys if k not in pref)
    seq = pref + rest
    return ", ".join(f"{k}×{int(summary[k])}" for k in seq) if seq else "empty"
