# glyph_813 – QUANTUM_TESSELLATION_ENGINE
# Even/odd tessellation pass to improve cache locality.

def glyph_813(seq):
    """
    Returns sequence reordered with evens first, odds second (by index).
    """
    evens = [x for i, x in enumerate(seq) if i % 2 == 0]
    odds  = [x for i, x in enumerate(seq) if i % 2 == 1]
    return evens + odds
