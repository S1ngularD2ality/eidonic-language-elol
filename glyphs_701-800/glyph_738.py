# glyph_738 – POLICY_LINTER
# Lint policy documents for duplicate IDs and unreachable rules.

def glyph_738(policies):
    """
    policies: list[{'id':str,'when':str,'allow':bool}]
    Returns: {'duplicates':[ids],'empty_when':[ids]}
    """
    seen, dup, empty = set(), [], []
    for p in policies:
        pid = p.get('id')
        if pid in seen:
            dup.append(pid)
        else:
            seen.add(pid)
        if not p.get('when'):
            empty.append(pid)
    return {"duplicates": dup, "empty_when": empty}
