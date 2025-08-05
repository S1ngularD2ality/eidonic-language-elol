def glyph_153(grid):
    """
    Counts how many values in the grid are divisible by 3.

    Example:
    Input: [[1,3,6],[7,9,10]]
    Output: 3
    """
    return sum(1 for row in grid for val in row if val % 3 == 0)
