def glyph_299(lst):
    """
    Glyph 299 — Singularity Isolation Engine
    Returns elements that appear only once.

    Example Input:
    [1,2,2,3,4,4,5]

    Output:
    [1,3,5]
    """
    return [x for x in lst if lst.count(x) == 1]
