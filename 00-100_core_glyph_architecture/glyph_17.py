def strip_sequence(grid):
    """
    Flattens a 2D symbolic structure into a linear strip.

    Parameters:
        grid (List[List[int]]): 2D symbolic array.

    Returns:
        List[int]: Flattened sequence.
    """
    return [cell for row in grid for cell in row]
