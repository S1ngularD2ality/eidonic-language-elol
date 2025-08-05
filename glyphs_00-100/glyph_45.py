def locate_targets(grid, symbol):
    """
    Finds coordinates of target symbol in a grid.

    Parameters:
        grid (List[List[int]]): Symbol matrix.
        symbol (int): Search value.

    Returns:
        List[Tuple[int, int]]: Positions found.
    """
    return [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == symbol]
