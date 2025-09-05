def glyph_214(events):
    """
    Glyph 214 — Chrono Trace Filter
    Filters a sequence of timestamped events by removing out-of-order anomalies.

    Example Input:
    [1, 3, 2, 4, 5]

    Output:
    [1, 3, 4, 5]
    """
    filtered = [events[0]]
    for i in range(1, len(events)):
        if events[i] >= filtered[-1]:
            filtered.append(events[i])
    return filtered
