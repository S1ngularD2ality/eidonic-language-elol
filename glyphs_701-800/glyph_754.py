# glyph_754 – STALE_DATA_PRUNER
# Remove outdated entries from a dataset.

import time

def glyph_754(entries, max_age_seconds):
    """
    entries: list of {'timestamp':float, 'data':...}
    Returns: pruned list
    """
    now = time.time()
    return [e for e in entries if now - e['timestamp'] <= max_age_seconds]
