def glyph_294(n):
    """
    Glyph 294 — Pulse Range Splitter
    Splits a range into evens and odds.

    Example Input:
    5

    Output:
    ([0,2,4], [1,3])
    """
    return ([i for i in range(n) if i % 2 == 0],
            [i for i in range(n) if i % 2 != 0])
