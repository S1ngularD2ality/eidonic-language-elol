def glyph_159(a, b):
    """
    Merges two lists by alternating elements. Pads shorter one with None.

    Example:
    Input: [1,3,5], [2,4]
    Output: [1,2,3,4,5,None]
    """
    result = []
    for i in range(max(len(a), len(b))):
        result.append(a[i] if i < len(a) else None)
        result.append(b[i] if i < len(b) else None)
    return result
