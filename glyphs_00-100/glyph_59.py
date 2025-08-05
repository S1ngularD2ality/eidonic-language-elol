def inverted_pulse(n):
    """
    Recursively counts inward from n to 1 and returns reversed list.

    Parameters:
        n (int): Start point.

    Returns:
        List[int]: Inverted pulse cascade.
    """
    if n <= 0:
        return []
    return [n] + inverted_pulse(n - 1)
