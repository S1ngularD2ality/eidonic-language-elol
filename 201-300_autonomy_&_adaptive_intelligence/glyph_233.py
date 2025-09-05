def glyph_233(data):
    """
    Glyph 233 — Fractal Step Filter
    Outputs every nth step where n increases with index.

    Example Input:
    [10, 20, 30, 40, 50, 60]

    Output:
    [10, 20, 40]
    """
    result = []
    i, step = 0, 1
    while i < len(data):
        result.append(data[i])
        i += step
        step += 1
    return result
