# glyph_150.py — Flame Indexer Loop
# -----------------------------------------------------------------------------
# ID:            150
# Pack:          Pack 002 (101–200)
# Name:          Flame Indexer Loop
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_150(n: int, *, start: int = 0) -> list[int]:
    """
    Flame Indexer Loop — emit cyclic indices 0..n-1 starting at `start`.

    Overview
    --------
    Produces [start, start+1, …] modulo n; returns empty list if n <= 0.

    Parameters
    ----------
    n : int
    start : int, optional (default: 0)

    Returns
    -------
    list[int]
        Loop indices.

    Examples
    --------
    >>> glyph_150(4, start=2)
    [2, 3, 0, 1]
    """
    if n <= 0: return []
    s = ((start % n) + n) % n
    return [(s + i) % n for i in range(n)]
