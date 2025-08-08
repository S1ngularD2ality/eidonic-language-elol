# glyph_736 – LATENT_SPACE_DRIFT
# Track distribution of embedding magnitudes and flag shifts.

import statistics
import math

class glyph_736:
    def __init__(self):
        self.ref_mean = None
        self.ref_std = None

    def _mag(self, vec):
        return math.sqrt(sum(v*v for v in vec))

    def fit(self, embeddings):
        mags = [self._mag(e) for e in embeddings]
        self.ref_mean = statistics.mean(mags)
        self.ref_std = statistics.pstdev(mags) or 1e-9

    def check(self, embeddings, z_thresh=3.0):
        if self.ref_mean is None:
            return {"mean_z": 0.0, "std_ratio": 1.0, "drift": False}
        mags = [self._mag(e) for e in embeddings]
        cur_mean = statistics.mean(mags)
        mean_z = abs((cur_mean - self.ref_mean) / self.ref_std)
        std_ratio = (statistics.pstdev(mags) or 1e-9) / self.ref_std
        return {"mean_z": mean_z, "std_ratio": std_ratio, "drift": mean_z > z_thresh or std_ratio > 2.0}
