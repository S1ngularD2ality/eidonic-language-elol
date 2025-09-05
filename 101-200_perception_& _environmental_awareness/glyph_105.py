def glyph_105(matrix):
    """
    Transforms input by prime factor encoding: returns 1 if prime, 0 otherwise.
    """
    def is_prime(n):
        if n <= 1: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    return [[1 if is_prime(cell) else 0 for cell in row] for row in matrix]
