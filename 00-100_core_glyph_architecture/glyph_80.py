def vortex_fork(n):
    """
    Generates dual outward spirals.

    Parameters:
        n (int)

    Returns:
        Tuple[List[int], List[int]]
    """
    return ([i for i in range(n)], [i**2 for i in range(n)])
