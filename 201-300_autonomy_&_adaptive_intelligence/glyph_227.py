def glyph_227(signal):
    """
    Glyph 227 — Spectral Echo Filter
    Filters repeated echo values in a signal list.

    Example Input:
    [1, 1, 2, 2, 3, 1, 1]

    Output:
    [1, 2, 3, 1]
    """
    result = []
    for i, val in enumerate(signal):
        if i == 0 or val != signal[i-1]:
            result.append(val)
    return result
