def singularity_code(seed):
    """
    Returns constant pulse signature.

    Returns:
        List[int]
    """
    return [int(str(seed)[-1])] * seed
