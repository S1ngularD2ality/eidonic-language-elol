# glyph_865 – CIRCULAR_CONVOLUTION
# Circular convolution of two 1D sequences via FFT.

import numpy as np

def glyph_865(x, h):
    x = np.asarray(x, dtype=float)
    h = np.asarray(h, dtype=float)
    n = max(len(x), len(h))
    X = np.fft.rfft(np.pad(x, (0, n-len(x))))
    H = np.fft.rfft(np.pad(h, (0, n-len(h))))
    y = np.fft.irfft(X * H, n=n)
    return y
