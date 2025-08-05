def pulse_sync(n, interval):
    """
    Marks beacon points in time.

    Parameters:
        n (int), interval (int)

    Returns:
        List[int]
    """
    return [1 if i % interval == 0 else 0 for i in range(n)]
