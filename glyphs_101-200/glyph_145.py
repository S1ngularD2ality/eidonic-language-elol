def glyph_145(grid):
    """
    Finds the absolute difference of each element from the central point (manhattan distance).

    Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[4,3,2],[3,2,3],[2,3,4]]
    """
    n = len(grid)
    m = len(grid[0])
    center_x, center_y = n//2, m//2
    return [[abs(i - center_x) + abs(j - center_y) for j in range(m)] for i in range(n)]
