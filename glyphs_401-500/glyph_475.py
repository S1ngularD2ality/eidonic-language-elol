# glyph_475 – MISSION_LOCK
# Lock a mission objective to prevent changes mid-operation

def glyph_475(mission, locked=True):
    """
    mission: dict with 'objective' key
    locked: bool
    Returns: updated mission
    """
    mission['locked'] = locked
    return mission
