def polarity_anchor(arr):
    """
    Detects central value closest to zero (anchor).

    Parameters:
        arr (List[int]): Symbolic polar values.

    Returns:
        int: Value closest to equilibrium.
    """
    return min(arr, key=lambda x: abs(x))
