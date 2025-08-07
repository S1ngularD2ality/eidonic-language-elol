# glyph_452 – TASK_CHAIN
# Link tasks so completion of one triggers the next

def glyph_452(tasks):
    """
    tasks: list of callables
    Returns: results list
    """
    results = []
    for t in tasks:
        results.append(t())
    return results
