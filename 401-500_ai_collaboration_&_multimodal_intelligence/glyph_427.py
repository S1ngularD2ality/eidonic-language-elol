# glyph_427 – LINK_CHECK
# Verify all data links and communication paths between agents

def glyph_427(links):
    """
    links: dict of agent:link_status (True/False)
    Returns: True if all good, False if any broken
    """
    return all(links.values())
