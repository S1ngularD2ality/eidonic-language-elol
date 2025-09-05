def glyph_104(matrix):
    """
    Sums each quadrant and returns a 2x2 summary matrix.
    """
    n = len(matrix)
    half = n // 2
    q1 = sum(sum(row[:half]) for row in matrix[:half])
    q2 = sum(sum(row[half:]) for row in matrix[:half])
    q3 = sum(sum(row[:half]) for row in matrix[half:])
    q4 = sum(sum(row[half:]) for row in matrix[half:])
    return [[q1, q2], [q3, q4]]
