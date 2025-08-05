def glyph_164(n):
    """
    Fills an n x n matrix in a clockwise spiral.

    Example:
    Input: 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]
    """
    matrix = [[0]*n for _ in range(n)]
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    x = y = d = 0
    for i in range(1, n*n + 1):
        matrix[x][y] = i
        nx, ny = x + dirs[d][0], y + dirs[d][1]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d + 1) % 4
            x += dirs[d][0]
            y += dirs[d][1]
    return matrix
