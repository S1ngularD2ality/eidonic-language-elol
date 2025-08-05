def resonance_ping(n):
    """
    Simulates periodic pinging in a resonance array.

    Parameters:
        n (int): Length of array.

    Returns:
        List[int]: Array with pings at intervals of 3.
    """
    return [1 if i % 3 == 0 else 0 for i in range(n)]
