def glyph_280(matrix):
    """
    Glyph 280 — Edge Divergence Mapper
    Returns difference between edge sum and center value.

    Example Input:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

    Output:
    40 - 5 = 35
    """
    edge_sum = glyph_275(matrix)
    center = matrix[len(matrix)//2][len(matrix[0])//2]
    return edge_sum - center
