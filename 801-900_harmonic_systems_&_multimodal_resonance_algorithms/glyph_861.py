# glyph_861 – CHROMA_STFT
# Compute 12-bin chroma from magnitude spectrogram frames (Hz grid assumed linear).

import numpy as np

def glyph_861(frames_mag, sr, n_fft):
    """
    frames_mag: 2D array [frames, bins] magnitudes
    sr: sample rate
    n_fft: FFT size used to produce frames_mag
    Returns: chroma [frames, 12]
    """
    S = np.asarray(frames_mag, dtype=float)
    bins = S.shape[1]
    freqs = np.arange(bins) * sr / n_fft
    eps = 1e-12
    # map bins to pitch classes (A440 reference -> MIDI 69)
    midi = 69 + 12 * np.log2((freqs + eps) / 440.0)
    pc = np.mod(np.round(midi), 12).astype(int)
    chroma = np.zeros((S.shape[0], 12), dtype=float)
    for b in range(bins):
        if freqs[b] < 20:  # ignore sub-audio
            continue
        chroma[:, pc[b]] += S[:, b]
    # normalize per frame
    chroma_sum = chroma.sum(axis=1, keepdims=True) + eps
    return chroma / chroma_sum
