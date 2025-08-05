def stitch_pairs(a, b):
    """
    Interlaces two arrays element-wise.

    Parameters:
        a (List[int]), b (List[int]): Input arrays.

    Returns:
        List[int]: Interwoven array.
    """
    return [val for pair in zip(a, b) for val in pair]
