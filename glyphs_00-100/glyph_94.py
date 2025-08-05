def mask_filter(arr, mask):
    """
    Filters only values that match resonance mask.

    Returns:
        List[int]
    """
    return [x for x, m in zip(arr, mask) if m]
