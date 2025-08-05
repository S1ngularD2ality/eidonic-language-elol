def glyph_188(n):
    """
    Constructs a list of 2^i from i = 0 to n-1.

    Example:
    Input: 4
    Output: [1,2,4,8]
    """
    return [2**i for i in range(n)]
