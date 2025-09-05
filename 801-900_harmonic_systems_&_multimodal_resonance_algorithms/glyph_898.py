# glyph_898 – BIQUAD_APPLY
# Apply biquad filter to signal with given coeffs.

def glyph_898(signal, b, a):
    x = list(map(float, signal))
    y = [0.0]*len(x)
    b0,b1,b2 = b
    _,a1,a2 = a
    x1=x2=y1=y2=0.0
    for n in range(len(x)):
        v = b0*x[n] + b1*x1 + b2*x2 - a1*y1 - a2*y2
        y[n]=v; x2=x1; x1=x[n]; y2=y1; y1=v
    return y
