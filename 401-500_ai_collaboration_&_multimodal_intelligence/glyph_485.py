# glyph_485 – BRIDGE_GROUPS
# Bridge two separate agent groups for collaboration

def glyph_485(group_a, group_b):
    """
    group_a: list
    group_b: list
    Returns: merged group
    """
    return list(set(group_a + group_b))
