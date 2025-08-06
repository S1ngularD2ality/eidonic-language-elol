def glyph_251(chains):
    """
    Glyph 251 — Temporal Chain Reverser
    Reverses each nested chain individually and preserves structure.

    Example Input:
    [[1, 2, 3], [4, 5]]

    Output:
    [[3, 2, 1], [5, 4]]
    """
    return [sub[::-1] for sub in chains]
