# glyph_756 – EVENT_CORRELATOR
# Correlate events by shared identifiers.

def glyph_756(events):
    """
    events: list of {'id':str,'type':str}
    Returns: dict id -> set of types
    """
    result = {}
    for e in events:
        result.setdefault(e['id'], set()).add(e['type'])
    return result
