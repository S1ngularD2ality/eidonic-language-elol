# glyph_748 – CONTEXTUAL_ERROR_CLASSIFIER
# Categorize errors based on execution context.

def glyph_748(errors):
    """
    errors: list[{'msg':str,'context':str}]
    Returns: dict context -> list of messages
    """
    classified = {}
    for e in errors:
        classified.setdefault(e['context'], []).append(e['msg'])
    return classified
