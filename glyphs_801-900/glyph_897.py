# glyph_897 – BIQUAD_COEFFS
# Compute biquad filter coefficients (RBJ cookbook).

import math

def glyph_897(kind, fs, f0, Q=0.707, gain_db=0.0):
    A = 10**(gain_db/40)
    w0 = 2*math.pi*f0/fs
    alpha = math.sin(w0)/(2*Q)
    cosw = math.cos(w0)

    if kind == "lpf":
        b0 = (1 - cosw)/2; b1 = 1 - cosw; b2 = (1 - cosw)/2
        a0 = 1 + alpha; a1 = -2*cosw; a2 = 1 - alpha
    elif kind == "hpf":
        b0 = (1 + cosw)/2; b1 = -(1 + cosw); b2 = (1 + cosw)/2
        a0 = 1 + alpha; a1 = -2*cosw; a2 = 1 - alpha
    elif kind == "peak":
        b0 = 1 + alpha*A; b1 = -2*cosw; b2 = 1 - alpha*A
        a0 = 1 + alpha/A; a1 = -2*cosw; a2 = 1 - alpha/A
    elif kind == "lowshelf":
        sqrtA = math.sqrt(A)
        b0 =    A*((A+1) - (A-1)*cosw + 2*sqrtA*alpha)
        b1 =  2*A*((A-1) - (A+1)*cosw)
        b2 =    A*((A+1) - (A-1)*cosw - 2*sqrtA*alpha)
        a0 =       (A+1) + (A-1)*cosw + 2*sqrtA*alpha
        a1 =   -2*((A-1) + (A+1)*cosw)
        a2 =       (A+1) + (A-1)*cosw - 2*sqrtA*alpha
    elif kind == "highshelf":
        sqrtA = math.sqrt(A)
        b0 =    A*((A+1) + (A-1)*cosw + 2*sqrtA*alpha)
        b1 = -2*A*((A-1) + (A+1)*cosw)
        b2 =    A*((A+1) + (A-1)*cosw - 2*sqrtA*alpha)
        a0 =       (A+1) - (A-1)*cosw + 2*sqrtA*alpha
        a1 =    2*((A-1) - (A+1)*cosw)
        a2 =       (A+1) - (A-1)*cosw - 2*sqrtA*alpha
    else:
        raise ValueError("Unknown kind")
    # normalize
    b0, b1, b2 = b0/a0, b1/a0, b2/a0
    a1, a2 = a1/a0, a2/a0
    return {"b":[b0,b1,b2], "a":[1.0,a1,a2]}
