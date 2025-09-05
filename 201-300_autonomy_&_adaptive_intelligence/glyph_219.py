def glyph_219(state_list, shift):
    """
    Glyph 219 — Oscillation State Shifter
    Applies a circular oscillation shift to a binary state list.

    Example Input:
    ([1, 0, 1], 1)

    Output:
    [0, 1, 1]
    """
    return state_list[-shift:] + state_list[:-shift]
