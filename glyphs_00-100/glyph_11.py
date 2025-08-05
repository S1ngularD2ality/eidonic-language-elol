def pulse_cycle(n):
    """
    Generates a repeating pulse sequence of increasing range.

    Parameters:
        n (int): Number of pulses.

    Returns:
        List[int]: Cyclic pulse pattern (e.g., [0,1,0,2,0,3,...])
    """
    return [j if i % 2 else 0 for i, j in enumerate(range(n))]
