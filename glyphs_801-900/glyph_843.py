# glyph_843 – TEMPO_FROM_AUTOCORR
# Estimate BPM from signal using autocorrelation peak search.

import numpy as np

def glyph_843(signal, sr, bpm_min=60, bpm_max=200):
    """
    signal: 1D array-like
    sr: sample rate (Hz)
    Returns: estimated BPM (float)
    """
    x = np.asarray(signal, dtype=float)
    x = x - x.mean()
    n = int(len(x))
    if n < sr:  # need at least 1s
        raise ValueError("Signal too short for tempo estimation.")
    # autocorr via FFT
    f = np.fft.rfft(x, n=2*n)
    p = f * np.conj(f)
    ac = np.fft.irfft(p)[:n]
    ac /= np.arange(n, 0, -1)  # unbiased
    # search lag bounds
    lag_min = int(sr*60.0/bpm_max)
    lag_max = int(sr*60.0/bpm_min)
    lag = np.argmax(ac[lag_min:lag_max]) + lag_min
    bpm = 60.0 * sr / lag
    return float(bpm)
