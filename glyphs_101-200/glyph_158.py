def glyph_158(grid, start_x, start_y, size):
    """
    Extracts a subgrid of given size starting from (start_x, start_y).

    Example:
    Input: grid, 0, 0, 2
    Output: [[grid[0][0], grid[0][1]], [grid[1][0], grid[1][1]]]
    """
    return [row[start_y:start_y+size] for row in grid[start_x:start_x+size]]
