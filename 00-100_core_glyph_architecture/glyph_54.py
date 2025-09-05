def dissolve_residue(grid, threshold):
    """
    Sets low-value pixels to 0.

    Parameters:
        grid (List[List[int]]): Symbol matrix.
        threshold (int): Minimum value to preserve.

    Returns:
        List[List[int]]: Cleansed matrix.
    """
    return [[cell if cell >= threshold else 0 for cell in row] for row in grid]
