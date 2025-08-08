# glyph_806 – METATRONIC_LOGIC_GATE
# Sacred-cube-inspired XOR-like decisor with bias toggle.

def glyph_806(a: bool, b: bool, bias: bool = False):
    """
    Returns XOR by default; if bias=True, prefers True on ties.
    """
    out = (a and not b) or (b and not a)
    return out or (bias and a == b)
