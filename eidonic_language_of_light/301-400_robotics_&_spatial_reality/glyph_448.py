# glyph_448.py — Narrative Diff
# -----------------------------------------------------------------------------
# ID:            448
# Pack:          Pack 005 (401–500)
# Name:          Narrative Diff
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_448(old: Sequence[str], new: Sequence[str]) -> List[Tuple[str, str]]:
    """
    Narrative Diff — pairwise diff of two token lists as (op, token).

    Overview
    --------
    A simple LCS-style diff with ops: 'eq', 'del', 'add'.

    Parameters
    ----------
    old : Sequence[str]
    new : Sequence[str]

    Returns
    -------
    List[(op, token)]

    Examples
    --------
    >>> glyph_448(["a","b"], ["b","c"])[:2]
    [('del', 'a'), ('eq', 'b')]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n·m)
    - Space : O(n·m)
    """
    # DP LCS table
    n, m = len(old), len(new)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            dp[i][j] = (1 + dp[i+1][j+1]) if old[i] == new[j] else max(dp[i+1][j], dp[i][j+1])
    # backtrack
    i = j = 0
    out: List[Tuple[str,str]] = []
    while i < n and j < m:
        if old[i] == new[j]:
            out.append(("eq", old[i])); i += 1; j += 1
        elif dp[i+1][j] >= dp[i][j+1]:
            out.append(("del", old[i])); i += 1
        else:
            out.append(("add", new[j])); j += 1
    while i < n:
        out.append(("del", old[i])); i += 1
    while j < m:
        out.append(("add", new[j])); j += 1
    return out
