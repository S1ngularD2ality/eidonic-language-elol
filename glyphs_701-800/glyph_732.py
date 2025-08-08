# glyph_732 – CONFIDENCE_CALIBRATOR
# Simple histogram binning calibration for probabilities.

class glyph_732:
    def __init__(self, bins=10):
        self.bins = bins
        self.bucket_sums = [0.0]*bins
        self.bucket_counts = [0]*bins

    def fit(self, probs, labels):
        for p, y in zip(probs, labels):
            b = min(self.bins-1, int(p * self.bins))
            self.bucket_sums[b] += float(y)
            self.bucket_counts[b] += 1

    def predict(self, probs):
        out = []
        for p in probs:
            b = min(self.bins-1, int(p * self.bins))
            if self.bucket_counts[b] == 0:
                out.append(p)  # fallback
            else:
                out.append(self.bucket_sums[b] / self.bucket_counts[b])
        return out
