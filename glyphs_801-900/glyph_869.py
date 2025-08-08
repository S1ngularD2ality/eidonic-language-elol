# glyph_869 – ISTFT
# Inverse STFT (overlap-add) for complex frames made by glyph_868.

import numpy as np

def glyph_869(stft_frames, n_fft=1024, hop=256, center=True, length=None):
    S = np.asarray(stft_frames, complex)
    win = np.hanning(n_fft)
    out_len = (S.shape[0]-1)*hop + n_fft
    y = np.zeros(out_len)
    wsum = np.zeros(out_len)
    for i, spec in enumerate(S):
        frame = np.fft.irfft(spec)
        start = i*hop
        y[start:start+n_fft] += frame * win
        wsum[start:start+n_fft] += win**2
    wsum[wsum == 0] = 1.0
    y /= wsum
    if center:
        pad = n_fft // 2
        y = y[pad:-pad]
    if length is not None:
        if len(y) < length:
            y = np.pad(y, (0, length-len(y)))
        else:
            y = y[:length]
    return y.astype(np.float32)
