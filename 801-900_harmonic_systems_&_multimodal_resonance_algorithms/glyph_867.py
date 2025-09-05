# glyph_867 – SPECTRAL_WHITENING
# Flatten spectrum by dividing by smoothed magnitude envelope.

import numpy as np

def glyph_867(mag, smooth=9):
    """
    mag: [frames, bins] or [bins]
    Returns same shape, whitened.
    """
    M = np.asarray(mag, float)
    if M.ndim == 1:
        M = M[None, :]
    k = max(1, smooth)
    kernel = np.ones(k)/k
    env = np.apply_along_axis(lambda v: np.convolve(v, kernel, mode='same'), 1, M)
    W = M / (env + 1e-12)
    return W if mag.ndim == 2 else W[0]
