def echo_propagate(grid, steps):
    """
    Propagates non-zero values outward across steps.

    Parameters:
        grid (List[List[int]]): Input matrix.
        steps (int): Number of echo rounds.

    Returns:
        List[List[int]]: Propagated grid.
    """
    from copy import deepcopy
    n, m = len(grid), len(grid[0])
    for _ in range(steps):
        new_grid = deepcopy(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni, nj = i+dx, j+dy
                        if 0 <= ni < n and 0 <= nj < m:
                            new_grid[ni][nj] = grid[i][j]
        grid = new_grid
    return grid
