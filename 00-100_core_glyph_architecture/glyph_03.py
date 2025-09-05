def rotate_inverse(grid):
    """
    Rotates and inverts a 2D grid by 90 degrees clockwise with horizontal mirroring.

    Parameters:
        grid (List[List[int]]): A 2D matrix representing symbolic data.

    Returns:
        List[List[int]]: A transformed matrix after rotation and reversal.
    """
    return [list(reversed(col)) for col in zip(*grid)]
