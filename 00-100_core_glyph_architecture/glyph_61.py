def reflection_frame(grid):
    """
    Produces a horizontally mirrored version of a matrix.

    Parameters:
        grid (List[List[int]]): Original frame.

    Returns:
        List[List[int]]: Reflected grid.
    """
    return [row[::-1] for row in grid]
