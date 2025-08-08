# glyph_833 – HEX_GRID_DISTANCE
# Compute distance on a hex grid using axial coordinates (q,r).

def glyph_833(a, b):
    """
    a,b: tuples (q,r)
    Returns hex distance (int).
    """
    aq, ar = a
    bq, br = b
    return int((abs(aq - bq) + abs(aq + ar - bq - br) + abs(ar - br)) / 2)
