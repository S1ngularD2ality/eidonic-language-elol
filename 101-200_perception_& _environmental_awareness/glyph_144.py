def glyph_144(grid):
    """
    Counts how many times adjacent values collapse into a lower number (left to right only).

    Example:
    Input: [[3, 2, 1], [4, 4, 3]]
    Output: 2
    """
    collapse = 0
    for row in grid:
        for i in range(len(row)-1):
            if row[i] > row[i+1]:
                collapse += 1
    return collapse
