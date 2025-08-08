# glyph_849 – HALTON_SEQUENCE
# Low-discrepancy 2D sequence (bases 2 and 3) for quasi-random sampling.

def _van_der_corput(n, base):
    vdc, denom = 0.0, 1.0
    while n:
        n, rem = divmod(n, base)
        denom *= base
        vdc += rem / denom
    return vdc

def glyph_849(count, start=0):
    """
    Returns list[(x,y)] of length `count` from Halton sequence.
    """
    pts = []
    for i in range(start, start+count):
        pts.append((_van_der_corput(i+1, 2), _van_der_corput(i+1, 3)))
    return pts
