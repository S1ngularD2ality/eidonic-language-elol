def glyph_229(states):
    """
    Glyph 229 — Echo State Bouncer
    Returns a new sequence where duplicates bounce to opposite polarity.

    Example Input:
    [1, 1, -1, -1, 1]

    Output:
    [1, -1, -1, 1, 1]
    """
    output = []
    toggle = 1
    for i, val in enumerate(states):
        if i > 0 and val == states[i-1]:
            toggle *= -1
            output.append(toggle * val)
        else:
            output.append(val)
    return output
