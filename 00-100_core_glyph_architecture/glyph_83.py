def lunar_harmony(days):
    """
    Creates lunar rhythm pattern across days.

    Parameters:
        days (int)

    Returns:
        List[str]
    """
    phases = ['🌑', '🌓', '🌕', '🌗']
    return [phases[i % 4] for i in range(days)]
