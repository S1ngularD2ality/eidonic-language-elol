# glyph_884 – HARMONIC_PRODUCT_SPECTRUM
# Estimate fundamental by peak of HPS on magnitude spectrum.

import numpy as np

def glyph_884(mag, sr, n_harm=4, fmin=60, fmax=1200):
    M = np.asarray(mag, float)
    H = M.copy()
    for h in range(2, n_harm+1):
        H[:len(M)//h] *= M[::h][:len(M)//h]
    freqs = np.linspace(0, sr/2, len(M))
    lo = np.searchsorted(freqs, fmin)
    hi = np.searchsorted(freqs, fmax)
    if hi - lo < 3: return 0.0
    k = lo + int(np.argmax(H[lo:hi]))
    return float(freqs[k])
