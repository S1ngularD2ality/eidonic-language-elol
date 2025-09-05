def radial_pulse(n):
    """
    Generates expanding radial waves.

    Parameters:
        n (int): Number of layers.

    Returns:
        List[List[int]]: Radial rings.
    """
    return [[i]*i for i in range(1, n+1)]
