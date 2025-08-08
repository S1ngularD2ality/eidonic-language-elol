# glyph_873 – MFCC
# Compute MFCCs from magnitude spectrogram using mel filterbank + DCT-II.

import numpy as np

def glyph_873(frames_mag, mel_fb, n_mfcc=13, eps=1e-10):
    """
    frames_mag: [frames, bins] magnitude
    mel_fb: [n_mels, bins]
    returns [frames, n_mfcc]
    """
    S = np.asarray(frames_mag, float)
    E = np.dot(S, mel_fb.T) + eps
    L = np.log(E)
    # DCT-II
    F = L.shape[1]
    k = np.arange(n_mfcc)[:, None]
    n = np.arange(F)[None, :]
    dct = np.sqrt(2/F) * np.cos(np.pi*(n + 0.5)*k/F)
    dct[0, :] *= 1/np.sqrt(2)
    return np.dot(L, dct.T)
