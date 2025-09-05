# glyph_737 – REPAIR_SUGGESTER
# Suggest repair strategies based on error signatures.

def glyph_737(error_msgs):
    """
    Returns dict signature->suggestion
    """
    suggestions = {}
    for e in error_msgs:
        e_low = e.lower()
        if "timeout" in e_low:
            suggestions[e] = "Increase timeout or optimize the slow path."
        elif "memory" in e_low:
            suggestions[e] = "Reduce batch size or free caches; check leak watcher."
        elif "permission" in e_low:
            suggestions[e] = "Verify credentials and file/network permissions."
        elif "not found" in e_low:
            suggestions[e] = "Check resource paths and initialization order."
        else:
            suggestions[e] = "Enable debug logs and rerun with minimal repro."
    return suggestions
