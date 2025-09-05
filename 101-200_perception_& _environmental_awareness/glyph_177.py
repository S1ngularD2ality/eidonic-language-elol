def glyph_177(grid):
    """
    Sums all even and odd numbers separately.

    Example:
    Input: [[1,2],[3,4]]
    Output: (Even: 6, Odd: 4)
    """
    evens, odds = 0, 0
    for row in grid:
        for val in row:
            if val % 2 == 0:
                evens += val
            else:
                odds += val
    return {'even': evens, 'odd': odds}
