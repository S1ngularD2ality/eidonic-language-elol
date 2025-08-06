def glyph_242(arr, delay):
    """
    Glyph 242 — Temporal Delay Balancer
    Shifts elements right by delay units, wrapping remainder.

    Example Input:
    ([1, 2, 3, 4], 2)

    Output:
    [3, 4, 1, 2]
    """
    delay %= len(arr)
    return arr[-delay:] + arr[:-delay]
