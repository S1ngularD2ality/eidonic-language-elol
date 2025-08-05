def timefold(n):
    """
    Alternates values by parity, folding linear time into up/down sequence.

    Parameters:
        n (int): Number of steps.

    Returns:
        List[int]: Parity-folded symbolic sequence.
    """
    return [i**2 if i % 2 == 0 else -i for i in range(n)]
