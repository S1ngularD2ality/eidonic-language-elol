# glyph_850 – SPECTRAL_PEAK_TRACK
# Track top-N magnitude peaks per frame.

import numpy as np

def glyph_850(spec_frames, topn=5, neighborhood=3):
    """
    spec_frames: 2D array [frames, freq_bins] magnitudes
    returns list of lists of (bin, mag)
    """
    S = np.asarray(spec_frames, dtype=float)
    out = []
    for f in range(S.shape[0]):
        row = S[f]
        peaks = []
        for i in range(neighborhood, len(row)-neighborhood):
            if row[i] == max(row[i-neighborhood:i+neighborhood+1]):
                peaks.append((i, row[i]))
        peaks.sort(key=lambda x: x[1], reverse=True)
        out.append(peaks[:topn])
    return out
