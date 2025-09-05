def logic_weave(arr, mod):
    """
    Interlaces values using modular wrap.

    Returns:
        List[int]
    """
    return [x % mod for x in arr]
