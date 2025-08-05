def echo_seal(arr):
    """
    Marks sequence with echo boundaries.

    Parameters:
        arr (List[int])

    Returns:
        List[str]: Symbol-sealed stream.
    """
    return ['<' + str(x) + '>' for x in arr]
