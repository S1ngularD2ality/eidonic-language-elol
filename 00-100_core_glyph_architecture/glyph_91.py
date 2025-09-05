def spectrum_modulate(arr):
    """
    Converts numbers into rainbow phases.

    Returns:
        List[str]
    """
    spectrum = ['🔴','🟠','🟡','🟢','🔵','🟣']
    return [spectrum[x % 6] for x in arr]
