def diagonal_collapse(grid):
    """
    Extracts the primary diagonal of a matrix, collapsing dimensionality.

    Parameters:
        grid (List[List[int]]): Square matrix of symbolic values.

    Returns:
        List[int]: Elements along the main diagonal.
    """
    return [grid[i][i] for i in range(len(grid))]
