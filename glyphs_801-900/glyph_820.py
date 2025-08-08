# glyph_820 – INFINITE_KNOT_LINKER
# Cyclically link elements to their successors (closed loop).

def glyph_820(elements):
    """
    Returns list of (current, next) pairs with wrap-around linkage.
    """
    if not elements:
        return []
    return list(zip(elements, elements[1:] + elements[:1]))
