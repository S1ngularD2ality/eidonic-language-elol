# glyph_864 – INSTANTANEOUS_FREQUENCY
# Estimate instantaneous frequency from phase differences (radians/frame).

import numpy as np

def glyph_864(phases, hop, sr, n_fft):
    """
    phases: [frames, bins] wrapped radians
    hop: hop length (samples)
    sr: sample rate
    n_fft: FFT size
    Returns: freq_hz [frames-1, bins]
    """
    P = np.unwrap(np.asarray(phases, float), axis=0)
    dphi = np.diff(P, axis=0)
    omega_k = 2*np.pi*np.arange(P.shape[1]) / n_fft
    # expected phase advance
    exp_adv = hop * omega_k
    # deviation -> frequency correction
    inst = sr/(2*np.pi) * (dphi - exp_adv)
    freq = (omega_k*(sr/(2*np.pi)))[None, :] + inst
    return freq
