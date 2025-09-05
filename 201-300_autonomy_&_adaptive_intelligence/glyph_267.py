def glyph_267(matrix):
    """
    Glyph 267 — Spatial Mirror Beacon
    Returns True if the matrix is symmetric across main diagonal.

    Example Input:
    [[1, 2],
     [2, 1]]

    Output:
    True
    """
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix[0])))
