# glyph_841 – HILBERT_INDEX_2D
# Map 2D integer coordinates to Hilbert curve index at order p, and back.

def _rot(n, x, y, rx, ry):
    if ry == 0:
        if rx == 1:
            x = n - 1 - x
            y = n - 1 - y
        # Swap x and y
        x, y = y, x
    return x, y

def glyph_841_xy2d(p: int, x: int, y: int) -> int:
    """
    p: order (grid size = 2**p)
    x,y: integer coords in [0, 2**p - 1]
    returns Hilbert index d
    """
    n = 1 << p
    d = 0
    s = n >> 1
    xx, yy = x, y
    while s > 0:
        rx = 1 if (xx & s) else 0
        ry = 1 if (yy & s) else 0
        d += s * s * ((3 * rx) ^ ry)
        xx, yy = _rot(s, xx, yy, rx, ry)
        s >>= 1
    return d

def glyph_841_d2xy(p: int, d: int) -> tuple[int, int]:
    """
    Inverse: map Hilbert index to (x,y) at order p.
    """
    n = 1 << p
    x = y = 0
    t = d
    s = 1
    while s < n:
        rx = 1 & (t // 2)
        ry = 1 & (t ^ rx)
        x, y = _rot(s, x, y, rx, ry)
        x += s * rx
        y += s * ry
        t //= 4
        s <<= 1
    return x, y
