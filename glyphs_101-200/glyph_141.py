def glyph_141(grid):
    """
    Splits a 2D grid of numbers into two separate lists: one for even numbers, one for odd numbers.
    Each row is flattened before processing.

    Example:
    Input: [[1, 4], [3, 2]]
    Output: ([4, 2], [1, 3])
    """
    flat = [cell for row in grid for cell in row]
    evens = [x for x in flat if x % 2 == 0]
    odds = [x for x in flat if x % 2 == 1]
    return evens, odds
