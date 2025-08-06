def glyph_253(n):
    """
    Glyph 253 — Singular Pulse Generator
    Creates a list pulsing outward from a center point.

    Example Input:
    5

    Output:
    [1, 2, 3, 2, 1]
    """
    return [i+1 if i <= n//2 else n-i for i in range(n)]
