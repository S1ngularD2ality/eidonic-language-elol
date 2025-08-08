# glyph_830 – TETRA_STABILITY_BALANCER
# Balance four channels to share total energy evenly.

def glyph_830(a, b, c, d):
    """
    Returns balanced tuple (a', b', c', d') with same total sum but equalized.
    """
    total = a + b + c + d
    q = total / 4.0
    return (q, q, q, q)
