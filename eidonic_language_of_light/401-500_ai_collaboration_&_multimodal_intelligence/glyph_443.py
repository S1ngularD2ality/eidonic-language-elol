# glyph_443.py — Recall Weave
# -----------------------------------------------------------------------------
# ID:            443
# Pack:          Pack 005 (401–500)
# Name:          Recall Weave
# Class:         memory
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_443(snippets: Sequence[str], *, max_tokens: int = 2048) -> List[str]:
    """
    Recall Weave — build a rolling context up to a token budget (proxy by chars).

    Overview
    --------
    Greedy-append snippets (de-duplicated) until length limit is reached.

    Parameters
    ----------
    snippets   : Sequence[str]
    max_tokens : int, optional (default: 2048) — approximated as characters.

    Returns
    -------
    List[str] : the kept snippets in order.

    Examples
    --------
    >>> glyph_443(["a","b","a","c"], max_tokens=2)
    ['a']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    seen = set()
    out: List[str] = []
    used = 0
    for s in snippets:
        s = str(s)
        if s in seen:
            continue
        if used + len(s) > max_tokens:
            break
        seen.add(s); out.append(s); used += len(s)
    return out
