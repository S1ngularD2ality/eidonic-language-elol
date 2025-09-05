def mirror_bloom(n):
    """
    Generates a self-replicating, mirrored sequence.

    Parameters:
        n (int): Depth of recursion.

    Returns:
        List[int]: Symmetrical bloom from recursion.
    """
    if n == 0:
        return []
    return mirror_bloom(n-1) + [n] + mirror_bloom(n-1)
