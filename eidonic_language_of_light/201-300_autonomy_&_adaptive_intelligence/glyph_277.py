# glyph_277.py — Spiral Index Translator
# -----------------------------------------------------------------------------
# ID:            277
# Pack:          Pack 003 (201–300)
# Original Name: Spiral Index Translator
# Manifest Name: Spiral Index Translator
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
def glyph_277(n: int, *, clockwise: bool = True) -> list[list[int]]:
    """
    Spiral Index Translator — map 0..n²−1 into a spiral layout grid.

    Overview
    --------
    Returns an n×n grid whose cells are the traversal order indices.

    Parameters
    ----------
    n : int
    clockwise : bool, optional (default: True)

    Returns
    -------
    list[list[int]]
        Spiral index grid.

    Examples
    --------
    >>> grid = glyph_277(3)
    >>> len(grid), len(grid[0])
    (3, 3)

    Exceptions
    ----------
    - ValueError : if n < 1.

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n^2)
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    grid = [[0]*n for _ in range(n)]
    c = n // 2
    x = y = c
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    if not clockwise:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    val = 0
    grid[y][x] = val; val += 1
    step = 1
    while val < n*n:
        for dxi, dyi in dirs:
            for _ in range(step):
                if val >= n*n: break
                x += dxi; y += dyi
                if 0 <= x < n and 0 <= y < n:
                    grid[y][x] = val; val += 1
            if (dxi, dyi) in (dirs[1], dirs[3]):
                step += 1
    return grid
