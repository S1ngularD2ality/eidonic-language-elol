# glyph_871 – WINDOW_FACTORY
# Generate common analysis windows: 'hann','hamming','blackman','rect'.

import numpy as np

def glyph_871(kind, N):
    kind = kind.lower()
    if N <= 0: return np.zeros(0)
    if kind == "hann":
        return np.hanning(N)
    if kind == "hamming":
        return np.hamming(N)
    if kind == "blackman":
        return np.blackman(N)
    if kind == "rect":
        return np.ones(N)
    raise ValueError("Unknown window kind.")
