def glyph_246(n):
    """
    Glyph 246 — Anchor Spiral Generator
    Generates a rightward spiral matrix of size n x n.

    Example Input:
    3

    Output:
    [[1, 2, 3],
     [8, 9, 4],
     [7, 6, 5]]
    """
    matrix = [[0]*n for _ in range(n)]
    dx, dy = 0, 1
    x, y = 0, 0
    for i in range(1, n*n+1):
        matrix[x][y] = i
        if matrix[(x+dx)%n][(y+dy)%n] != 0:
            dx, dy = dy, -dx
        x += dx
        y += dy
    return matrix
