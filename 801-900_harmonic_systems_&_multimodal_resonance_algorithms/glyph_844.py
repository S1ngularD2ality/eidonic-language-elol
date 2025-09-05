# glyph_844 – ONSET_SPECTRAL_FLUX
# Energy onsets via spectral flux with half-wave rectification + adaptive threshold.

import numpy as np

def glyph_844(signal, sr, frame=1024, hop=512, thresh_coef=1.5):
    """
    Returns onset frame indices.
    """
    x = np.asarray(signal, dtype=float)
    # STFT magnitude
    win = np.hanning(frame)
    mags = []
    for i in range(0, len(x)-frame+1, hop):
        seg = x[i:i+frame]*win
        spec = np.abs(np.fft.rfft(seg))
        mags.append(spec)
    mags = np.asarray(mags)
    flux = np.maximum(0, np.diff(mags, axis=0)).sum(axis=1)
    if len(flux) < 8:
        return []
    # adaptive threshold
    w = 8
    thr = np.convolve(flux, np.ones(w)/w, mode='same') * thresh_coef
    onsets = np.where(flux > thr)[0] + 1  # align to later frame
    # convert to frame indices (keep as frames)
    return onsets.tolist()
