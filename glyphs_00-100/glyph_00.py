def emergence_spiral(n):
    """
    Generates a list of values based on a harmonic emergence pattern.
    Includes squares incremented by their index if divisible by 3 or 5.

    Parameters:
        n (int): The upper limit of the range to evaluate.

    Returns:
        List[int]: A list of patterned values representing emergence points.
    """
    return [i**2 + i for i in range(n) if (i % 3 == 0 or i % 5 == 0)]
