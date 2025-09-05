def glyph_201(journey_map):
    """
    Glyph 201 — Pathlight Resonator
    Illuminates the next possible step in a grid-based journey map by 
    tracing light paths from current positions. 
    Ideal for AI path prediction and trajectory planning.

    Example Input:
    [[0, 1, 0],
     [0, 0, 0],
     [1, 0, 1]]

    Output:
    [(0, 1), (2, 0), (2, 2)]
    """
    next_steps = []
    for y, row in enumerate(journey_map):
        for x, val in enumerate(row):
            if val == 1:
                next_steps.append((y, x))
    return next_steps
