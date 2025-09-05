# glyph_479 – RESOLVE_LOOP
# Continuously resolve outstanding issues until none remain

def glyph_479(issues, resolver):
    """
    issues: list
    resolver: callable(issue) -> resolution
    Returns: list of resolutions
    """
    resolutions = []
    while issues:
        issue = issues.pop(0)
        resolutions.append(resolver(issue))
    return resolutions
