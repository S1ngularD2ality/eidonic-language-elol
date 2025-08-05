def glyph_162(n):
    """
    Builds a right-angle triangle grid of size n filled with ascending integers.

    Example:
    Input: 3
    Output: [[1],[2,3],[4,5,6]]
    """
    result, counter = [], 1
    for i in range(1, n + 1):
        row = [counter + j for j in range(i)]
        result.append(row)
        counter += i
    return result
