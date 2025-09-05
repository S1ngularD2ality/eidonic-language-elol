def glyph_292(matrix):
    """
    Glyph 292 — Core Fragment Equalizer
    Makes all rows equal length by truncating to the shortest.

    Example Input:
    [[1,2,3], [4,5]]

    Output:
    [[1,2], [4,5]]
    """
    length = min(len(row) for row in matrix)
    return [row[:length] for row in matrix]
