# glyph_721 – POLICY_DIFF_ANALYZER
# Compare two policy sets and report added/removed/changed rules.

def glyph_721(old_policies: dict, new_policies: dict):
    """
    Policies are dict[str, str] mapping rule_id -> rule_body (string).
    Returns: {'added': [ids], 'removed': [ids], 'changed': [ids]}
    """
    old_keys = set(old_policies.keys())
    new_keys = set(new_policies.keys())
    added = sorted(list(new_keys - old_keys))
    removed = sorted(list(old_keys - new_keys))
    changed = sorted([k for k in (old_keys & new_keys) if old_policies[k] != new_policies[k]])
    return {"added": added, "removed": removed, "changed": changed}
