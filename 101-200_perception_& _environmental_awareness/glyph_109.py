def glyph_109(matrix):
    """
    Applies a harmonic filter: each value becomes average of neighbors.
    """
    from statistics import mean
    def neighbors(x, y):
        return [matrix[i][j] for i in range(max(0, x-1), min(len(matrix), x+2))
                for j in range(max(0, y-1), min(len(matrix[0]), y+2)) if not (i == x and j == y)]
    return [[round(mean(neighbors(i, j))) for j in range(len(matrix[0]))] for i in range(len(matrix))]
