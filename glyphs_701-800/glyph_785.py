# glyph_785 – PROBABILITY_STABILITY_GUARD
# Monitors probability drift to ensure output stability.

def glyph_785(probabilities, tolerance=0.05):
    mean_prob = sum(probabilities) / len(probabilities)
    return all(abs(p - mean_prob) <= tolerance for p in probabilities)
