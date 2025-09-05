def glyph_215(arr):
    """
    Glyph 215 — Echo Pair Locator
    Identifies all mirrored value pairs in a sequence.

    Example Input:
    [1, 2, 3, 2, 1]

    Output:
    [(0, 4), (1, 3)]
    """
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and (j, i) not in pairs:
                pairs.append((i, j))
    return pairs
