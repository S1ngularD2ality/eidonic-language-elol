def xor_pattern(a, b):
    """
    Applies XOR operation element-wise between two 2D grids to reveal masked structures.

    Parameters:
        a (List[List[int]]): First input matrix.
        b (List[List[int]]): Second input matrix of the same dimensions.

    Returns:
        List[List[int]]: Resulting matrix after XOR comparison.
    """
    return [[ai ^ bi for ai, bi in zip(ar, br)] for ar, br in zip(a, b)]
