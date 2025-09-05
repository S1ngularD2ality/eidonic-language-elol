def extract_bright(grid, threshold):
    """
    Extracts positions of values above threshold.

    Parameters:
        grid (List[List[int]]): Input matrix.
        threshold (int): Value threshold.

    Returns:
        List[Tuple[int, int]]: Coordinates of bright zones.
    """
    return [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val > threshold]
