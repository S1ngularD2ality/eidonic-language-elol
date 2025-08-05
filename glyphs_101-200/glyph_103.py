def glyph_103(matrix):
    """
    Applies Fibonacci glyph patterning across rows.
    """
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n): a, b = b, a + b
        return a
    return [[fibonacci(cell) for cell in row] for row in matrix]
