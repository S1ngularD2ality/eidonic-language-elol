# glyph_870 – BEAT_GRID_FROM_ONSETS
# Derive BPM and beat grid from onset indices using autocorrelation.

import numpy as np

def glyph_870(onset_frames, sr, hop, bpm_min=60, bpm_max=200):
    """
    onset_frames: list[int] frame indices of onsets
    Returns dict(bpm, grid_times_sec)
    """
    if len(onset_frames) < 4:
        return {"bpm": 0.0, "grid_times_sec": []}
    x = np.zeros(max(onset_frames)+1)
    x[np.asarray(onset_frames, int)] = 1.0
    n = int(2**np.ceil(np.log2(len(x)*2)))
    F = np.fft.rfft(x, n)
    ac = np.fft.irfft(F*np.conj(F))[:len(x)]
    lag_min = int(sr*60/(hop*bpm_max))
    lag_max = int(sr*60/(hop*bpm_min))
    lag = np.argmax(ac[lag_min:lag_max]) + lag_min
    bpm = 60.0 * sr / (hop * lag)
    # build grid aligned to first onset
    start = onset_frames[0]
    frames = list(range(start, len(x), lag))
    times = [f*hop/sr for f in frames]
    return {"bpm": float(bpm), "grid_times_sec": times}
