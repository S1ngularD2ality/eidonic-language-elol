# glyph_808 – QUANTUM_DODECAHEDRON_ROUTER
# Route indices using a 5-fold jump pattern reminiscent of dodeca symmetry.

def glyph_808(nodes, start_index=0):
    """
    nodes: list
    Returns reordered view by stepping in 5s from start, then remaining.
    """
    n = len(nodes)
    if n == 0:
        return []
    step = 5 % n
    visited = []
    i = start_index % n
    seen = set()
    for _ in range(n):
        if i not in seen:
            visited.append(nodes[i])
            seen.add(i)
        i = (i + step) % n
    return visited
