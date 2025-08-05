def echo_trigger(n, trigger):
    """
    Emits echo signals on matching index.

    Returns:
        List[str]
    """
    return ['📡' if i == trigger else '-' for i in range(n)]
