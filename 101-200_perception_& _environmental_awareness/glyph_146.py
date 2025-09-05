def glyph_146(seq):
    """
    Splits a list into three equal parts. Pads with None if needed.

    Example:
    Input: [1,2,3,4,5,6,7]
    Output: [[1,2,3], [4,5,6], [7,None,None]]
    """
    length = len(seq)
    size = (length + 2) // 3
    return [seq[i:i+size] + [None]*(size - len(seq[i:i+size])) for i in range(0, length, size)]
