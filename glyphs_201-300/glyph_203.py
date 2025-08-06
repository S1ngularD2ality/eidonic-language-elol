def glyph_203(sequence):
    """
    Glyph 203 — Entropy Sequence Extractor
    Analyzes a list of values and returns the positions where entropy increases,
    defined by changes in local variance.

    Example Input:
    [2, 4, 4, 7, 9, 9, 5, 3]

    Output:
    [3, 6]
    """
    spikes = []
    for i in range(1, len(sequence) - 1):
        if abs(sequence[i] - sequence[i-1]) < abs(sequence[i+1] - sequence[i]):
            spikes.append(i+1)
    return spikes
