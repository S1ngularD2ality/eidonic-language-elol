def lockstep_encoder(a, b):
    """
    Encodes step-locked sequence.

    Returns:
        List[int]
    """
    return [ai * bi for ai, bi in zip(a, b)]
