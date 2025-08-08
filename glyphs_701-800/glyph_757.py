# glyph_757 – KNOWLEDGE_MERGE_RESOLVER
# Merge knowledge base entries with conflict resolution.

def glyph_757(base, updates):
    """
    base, updates: dict id->content
    Conflicts resolved by keeping longer entry.
    """
    merged = dict(base)
    for k, v in updates.items():
        if k not in merged or len(v) > len(merged[k]):
            merged[k] = v
    return merged
