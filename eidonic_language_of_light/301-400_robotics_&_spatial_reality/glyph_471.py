# glyph_471.py — Tie Resolver
# -----------------------------------------------------------------------------
# ID:            471
# Pack:          Pack 005 (401–500)
# Name:          Tie Resolver
# Class:         consensus
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_471(options: Sequence[str], *, prefer: Sequence[str] = ()) -> str:
    """
    Tie Resolver — deterministic choice by preference order then lexicographic.

    Overview
    --------
    Returns the first item present in `prefer`, else min(options).

    Parameters
    ----------
    options : Sequence[str]
    prefer  : Sequence[str]

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_471(["b","a"], prefer=["c","a"])
    'a'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(1)
    """
    prefs = [p for p in prefer if p in options]
    if prefs:
        return prefs[0]
    return min(options) if options else ""
