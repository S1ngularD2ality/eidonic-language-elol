# glyph_900 – SCHROEDER_REVERB
# Simple Schroeder reverb: 4 combs + 2 allpasses (mono).

import numpy as np

def _comb(x, delay, feedback, damp=0.0):
    buf = np.zeros(delay); y = np.zeros_like(x)
    zi = 0; last = 0.0
    for i, s in enumerate(x):
        out = buf[zi]
        last = (1 - damp)*out + damp*last
        buf[zi] = s + feedback*last
        y[i] = out
        zi = (zi + 1) % delay
    return y

def _allpass(x, delay, g):
    buf = np.zeros(delay); y = np.zeros_like(x)
    zi = 0
    for i, s in enumerate(x):
        v = s + (-g)*buf[zi]
        y[i] = buf[zi] + g*v
        buf[zi] = v
        zi = (zi + 1) % delay
    return y

def glyph_900(signal, sr, wet=0.3):
    x = np.asarray(signal, float)
    # comb delays ~ prime-ish around 30-45ms
    combs = [
        _comb(x, int(sr*0.0297), 0.805, 0.2),
        _comb(x, int(sr*0.0371), 0.827, 0.2),
        _comb(x, int(sr*0.0411), 0.783, 0.2),
        _comb(x, int(sr*0.0437), 0.764, 0.2),
    ]
    y = sum(combs) / len(combs)
    # allpasses ~ 5ms, 1.7ms
    y = _allpass(y, int(sr*0.005), 0.7)
    y = _allpass(y, int(sr*0.0017), 0.7)
    out = (1 - wet)*x + wet*y
    return out.astype(np.float32)
