# glyph_858 – IIR_FILTER_APPLY
# Apply causal IIR filter given coefficients a (den) and b (num), scipy-free.

def glyph_858(x, b, a):
    """
    x: input list/array
    b: numerator coeffs [b0..bM]
    a: denominator coeffs [1, a1..aN] (a[0] must be 1)
    returns y list
    """
    if not a or abs(a[0]-1.0) > 1e-12:
        raise ValueError("a[0] must be 1")
    y = [0.0]*len(x)
    for n in range(len(x)):
        acc = 0.0
        for k in range(len(b)):
            if n-k >= 0: acc += b[k]*x[n-k]
        for k in range(1, len(a)):
            if n-k >= 0: acc -= a[k]*y[n-k]
        y[n] = acc
    return y
