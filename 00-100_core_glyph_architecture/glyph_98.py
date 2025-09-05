def collapse_chain(arr):
    """
    Removes values that cancel each other.

    Returns:
        List[int]
    """
    stack = []
    for x in arr:
        if stack and stack[-1] + x == 0:
            stack.pop()
        else:
            stack.append(x)
    return stack
