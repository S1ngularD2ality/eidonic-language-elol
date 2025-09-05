def glyph_182(grid):
    """
    Pulls values toward the center, averaging neighboring cells.

    Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,2,3],[4,5,6],[7,8,9]] (center cell adjusted)
    """
    from copy import deepcopy
    result = deepcopy(grid)
    n = len(grid)
    for i in range(1, n-1):
        for j in range(1, n-1):
            neighbors = [
                grid[i-1][j], grid[i+1][j],
                grid[i][j-1], grid[i][j+1]
            ]
            result[i][j] = sum(neighbors) // len(neighbors)
    return result
