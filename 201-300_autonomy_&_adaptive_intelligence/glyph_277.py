def glyph_277(arr):
    """
    Glyph 277 — Core Thread Isolator
    Returns center element of list (or two if even).

    Example Input:
    [1, 2, 3, 4]

    Output:
    [2, 3]
    """
    mid = len(arr) // 2
    return arr[mid-1:mid+1] if len(arr) % 2 == 0 else [arr[mid]]
