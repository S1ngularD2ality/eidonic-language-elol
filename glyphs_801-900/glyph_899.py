# glyph_899 – ALLPASS_PHASE_SHIFTER
# First-order allpass filter for phase manipulation.

def glyph_899(signal, a=0.5):
    """
    0<a<1 for stability; returns phase-shifted signal.
    """
    x1=y1=0.0
    out=[]
    for x in map(float, signal):
        y = -a*x + x1 + a*y1
        out.append(y)
        x1 = x
        y1 = y
    return out
