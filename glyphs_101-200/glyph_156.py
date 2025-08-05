def glyph_156(grid):
    """
    Counts how many values are above the average of the entire grid.

    Example:
    Input: [[1,2,3],[4,5,6]]
    Output: 3
    """
    flat = [val for row in grid for val in row]
    avg = sum(flat) / len(flat)
    return sum(1 for val in flat if val > avg)
