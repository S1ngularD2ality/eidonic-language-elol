# glyph_746 – KNOWLEDGE_HYGIENE_CHECK
# Validate that knowledge base entries meet quality standards.

def glyph_746(entries):
    """
    entries: list[{'id':str,'content':str}]
    Returns: {'empty':[], 'short':[], 'ok':[]}
    """
    empty, short, ok = [], [], []
    for e in entries:
        if not e['content']:
            empty.append(e['id'])
        elif len(e['content']) < 50:
            short.append(e['id'])
        else:
            ok.append(e['id'])
    return {"empty": empty, "short": short, "ok": ok}
