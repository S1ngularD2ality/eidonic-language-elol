# glyph_805 – TORUS_FLOW_NETWORK
# Toroidal rotation of a sequence to prevent bottlenecks.

def glyph_805(seq, loops=1):
    """
    Rotates the sequence by 1 step, 'loops' times.
    """
    if not seq:
        return seq
    buf = list(seq)
    for _ in range(max(0, loops)):
        buf = buf[1:] + buf[:1]
    return buf
