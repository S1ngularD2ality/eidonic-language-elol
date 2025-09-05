# glyph_431 – SIGNAL_PRIORITY
# Assign priority to signals, tasks, or requests in a busy collective

def glyph_431(items):
    """
    items: list of (priority, task)
    Returns: sorted list by priority (high to low)
    """
    return sorted(items, key=lambda x: -x[0])
