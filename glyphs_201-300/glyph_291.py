def glyph_291(a, b):
    """
    Glyph 291 — Spectral Merge Walker
    Interleaves two lists, continuing whichever is longer.

    Example Input:
    [1,2,3], ['a','b']

    Output:
    [1,'a',2,'b',3]
    """
    result = []
    for i in range(max(len(a), len(b))):
        if i < len(a): result.append(a[i])
        if i < len(b): result.append(b[i])
    return result
