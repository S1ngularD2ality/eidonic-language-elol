# glyph_872 – MEL_FILTERBANK
# Create mel filterbank matrix [n_mels, n_fft//2+1].

import numpy as np

def _hz_to_mel(f): return 2595.0 * np.log10(1.0 + f/700.0)
def _mel_to_hz(m): return 700.0 * (10**(m/2595.0) - 1.0)

def glyph_872(sr, n_fft, n_mels=40, fmin=0.0, fmax=None):
    if fmax is None:
        fmax = sr/2
    mmin, mmax = _hz_to_mel(fmin), _hz_to_mel(fmax)
    mpts = np.linspace(mmin, mmax, n_mels+2)
    fpts = _mel_to_hz(mpts)
    bins = np.floor((n_fft+1) * fpts / sr).astype(int)
    fb = np.zeros((n_mels, n_fft//2 + 1))
    for m in range(1, n_mels+1):
        f_m_left, f_m, f_m_right = bins[m-1], bins[m], bins[m+1]
        for k in range(f_m_left, f_m):
            fb[m-1, k] = (k - f_m_left) / max(1, (f_m - f_m_left))
        for k in range(f_m, f_m_right):
            fb[m-1, k] = (f_m_right - k) / max(1, (f_m_right - f_m))
    return fb
