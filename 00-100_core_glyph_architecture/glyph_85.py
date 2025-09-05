def unpack_frames(matrix):
    """
    Flattens frozen frame matrix.

    Parameters:
        matrix (List[List[int]])

    Returns:
        List[int]
    """
    return [item for row in matrix for item in row]
