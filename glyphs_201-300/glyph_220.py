def glyph_220(matrix, limit):
    """
    Glyph 220 — Threshold Spiral Bloom
    Replaces all values above a threshold with spiral growth values.

    Example Input:
    ([[1, 5], [7, 2]], 4)

    Output:
    [[1, 1], [2, 2]]
    """
    count = 1
    output = []
    for row in matrix:
        new_row = []
        for val in row:
            if val > limit:
                new_row.append(count)
                count += 1
            else:
                new_row.append(val)
        output.append(new_row)
    return output
