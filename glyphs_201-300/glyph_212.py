def glyph_212(vectors):
    """
    Glyph 212 — Vector Constellation Sort
    Sorts vectors by their magnitude to simulate celestial alignment.

    Example Input:
    [[3, 4], [1, 1], [0, 5]]

    Output:
    [[1, 1], [0, 5], [3, 4]]
    """
    return sorted(vectors, key=lambda v: (v[0]**2 + v[1]**2)**0.5)
