def spiral_gradient(n):
    """
    Generates a square matrix filled with increasing integers in a spiral pattern.

    Parameters:
        n (int): The size of the NxN matrix.

    Returns:
        List[List[int]]: A spiral-ordered matrix.
    """
    matrix = [[0]*n for _ in range(n)]
    val = 1
    layers = (n+1)//2
    for l in range(layers):
        for i in range(l, n-l): matrix[l][i] = val; val += 1
        for i in range(l+1, n-l): matrix[i][n-l-1] = val; val += 1
        for i in range(n-l-2, l-1, -1): matrix[n-l-1][i] = val; val += 1
        for i in range(n-l-2, l, -1): matrix[i][l] = val; val += 1
    return matrix
