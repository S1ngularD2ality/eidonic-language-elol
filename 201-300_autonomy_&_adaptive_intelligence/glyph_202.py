def glyph_202(grid):
    """
    Glyph 202 — Quantum Mirror Fold
    Folds a square matrix along both diagonal mirrors to generate a mirrored pattern grid.

    Example Input:
    [[1, 2],
     [3, 4]]

    Output:
    [[1, 2, 2, 1],
     [3, 4, 4, 3],
     [3, 4, 4, 3],
     [1, 2, 2, 1]]
    """
    n = len(grid)
    folded = []
    for row in grid:
        folded.append(row + row[::-1])
    mirrored = folded + [row for row in reversed(folded)]
    return mirrored
