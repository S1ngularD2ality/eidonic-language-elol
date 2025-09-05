# glyph_809 – VESICA_PISCIS_BRIDGE
# Overlapping-field merge between two sequences.

def glyph_809(a, b):
    """
    Soft-merge: take first half of a and second half of b.
    """
    if not a and not b:
        return []
    mid_a = len(a) // 2
    mid_b = len(b) // 2
    return list(a[:mid_a]) + list(b[mid_b:])
