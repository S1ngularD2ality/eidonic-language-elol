# glyph_826 – LATTICE_PATH_COUNTER
# Count shortest lattice paths from (0,0) to (m,n) using binomial coefficients.

from math import comb

def glyph_826(m: int, n: int) -> int:
    """
    Number of monotonic paths on an m×n grid (only right/up moves): C(m+n, m).
    """
    if m < 0 or n < 0:
        raise ValueError("m,n >= 0")
    return comb(m + n, m)
