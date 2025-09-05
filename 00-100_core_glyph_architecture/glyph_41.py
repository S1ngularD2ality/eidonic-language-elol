def repeating_pulse(arr):
    """
    Extracts all repeating pulses in a signal.

    Parameters:
        arr (List[int]): Symbol signal.

    Returns:
        List[int]: Repeated elements.
    """
    seen = set()
    repeated = set()
    for x in arr:
        if x in seen:
            repeated.add(x)
        else:
            seen.add(x)
    return list(repeated)
