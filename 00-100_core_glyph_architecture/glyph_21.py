def axis_diverge(grid):
    """
    Compares horizontal and vertical sums of a 2D matrix.

    Parameters:
        grid (List[List[int]]): 2D matrix.

    Returns:
        Tuple[List[int], List[int]]: Row sums, Column sums.
    """
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    return row_sums, col_sums
