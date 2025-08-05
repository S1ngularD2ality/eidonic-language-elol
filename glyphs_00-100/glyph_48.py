def flip_invert(grid):
    """
    Flips grid horizontally and inverts binary values.

    Parameters:
        grid (List[List[int]]): Binary matrix.

    Returns:
        List[List[int]]: Transformed matrix.
    """
    return [[1 - cell for cell in reversed(row)] for row in grid]
