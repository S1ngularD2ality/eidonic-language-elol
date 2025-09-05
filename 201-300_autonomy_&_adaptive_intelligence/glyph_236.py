def glyph_236(seq):
    """
    Glyph 236 — Frequency Reflection Sorter
    Sorts values based on their frequency (descending), then value.

    Example Input:
    [4, 6, 2, 2, 6, 4, 4]

    Output:
    [4, 4, 4, 2, 2, 6, 6]
    """
    from collections import Counter
    counts = Counter(seq)
    return sorted(seq, key=lambda x: (-counts[x], x))
