# glyph_889 – COMPRESSOR_SIMPLE
# Static waveshaper compressor with soft knee.

import numpy as np

def glyph_889(signal, threshold=0.5, ratio=4.0, knee=0.1, makeup=1.0):
    x = np.asarray(signal, float)
    t = abs(x)
    # soft knee region
    lower = threshold - knee
    upper = threshold + knee
    y = np.empty_like(x)
    for i, a in enumerate(t):
        sign = 1 if x[i] >= 0 else -1
        if a <= lower:
            m = a
        elif a >= upper:
            m = threshold + (a - threshold)/ratio
        else:
            # quadratic interpolation in knee
            k = (a - lower)/(2*knee)
            m = lower + k*( (a - lower)/ratio + (a - lower) )
        y[i] = sign * m
    return (y * makeup).astype(np.float32)
