def flatten_depth(nested):
    """
    Flattens any level of nested list structures into a single-dimensional list.

    Parameters:
        nested (List[Any]): Arbitrarily nested list.

    Returns:
        List[Any]: Fully flattened version of the nested structure.
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_depth(item))
        else:
            result.append(item)
    return result
