# glyph_851 – RADIAL_POWER_SPECTRUM
# Radially averaged 2D power spectrum (texture/structure analysis).

import numpy as np

def glyph_851(image_2d):
    """
    image_2d: 2D array
    returns (radii, radial_power) as 1D arrays
    """
    I = np.asarray(image_2d, dtype=float)
    F = np.fft.fftshift(np.fft.fft2(I))
    P = (np.abs(F)**2)
    h, w = P.shape
    cy, cx = h//2, w//2
    y, x = np.indices(P.shape)
    r = np.hypot(x - cx, y - cy)
    r_int = r.astype(int)
    rmax = r_int.max()
    radial = np.zeros(rmax+1)
    counts = np.zeros(rmax+1)
    for i in range(h):
        for j in range(w):
            ri = r_int[i, j]
            radial[ri] += P[i, j]
            counts[ri] += 1
    counts[counts == 0] = 1
    return np.arange(rmax+1), radial / counts
