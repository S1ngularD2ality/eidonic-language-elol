# glyph_883 – BEAT_SYNC_AGG
# Aggregate frame features into beat-synchronous means.

import numpy as np

def glyph_883(features, beat_frames):
    """
    features: [frames, D]
    beat_frames: sorted list of frame indices (beat boundaries)
    returns [len(beat_frames)-1, D]
    """
    F = np.asarray(features, float)
    bf = list(beat_frames)
    out = []
    for a, b in zip(bf[:-1], bf[1:]):
        seg = F[a:b]
        if len(seg) == 0:
            out.append(np.zeros(F.shape[1]))
        else:
            out.append(seg.mean(axis=0))
    return np.array(out)
