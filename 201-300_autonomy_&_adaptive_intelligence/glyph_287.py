def glyph_287(matrix):
    """
    Glyph 287 — Celestial Grid Aligner
    Aligns rows of matrix by padding shorter ones with zeros.

    Example Input:
    [[1], [2, 3]]

    Output:
    [[1, 0],
     [2, 3]]
    """
    width = max(len(row) for row in matrix)
    return [row + [0]*(width - len(row)) for row in matrix]
