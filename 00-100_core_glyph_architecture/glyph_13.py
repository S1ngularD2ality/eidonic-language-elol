def echo_loop(arr, loops):
    """
    Recursively repeats the symbolic input multiple times.

    Parameters:
        arr (List[Any]): Symbolic sequence.
        loops (int): Number of echoes.

    Returns:
        List[Any]: Echoed sequence of the original input.
    """
    return arr * loops
