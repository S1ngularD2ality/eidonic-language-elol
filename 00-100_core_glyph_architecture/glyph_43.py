def block_count(grid, symbol):
    """
    Counts number of continuous blocks of a given symbol.

    Parameters:
        grid (List[List[int]]): 2D matrix.
        symbol (int): Target symbol.

    Returns:
        int: Count of blocks.
    """
    count = 0
    for row in grid:
        if symbol in row:
            count += 1
    return count
