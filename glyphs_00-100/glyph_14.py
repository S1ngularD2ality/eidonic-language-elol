def pulse_trail(n):
    """
    Recursively generates a trail of pulse markers from 0 to n.

    Parameters:
        n (int): End of pulse trail.

    Returns:
        List[int]: Pulse sequence tracing prior memory steps.
    """
    if n <= 1:
        return [n]
    else:
        return pulse_trail(n-1) + [n]
