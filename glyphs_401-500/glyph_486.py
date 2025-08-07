# glyph_486 – TASK_ESCALATE
# Escalate a task to higher-priority handling

def glyph_486(task, priority_levels):
    """
    task: string
    priority_levels: dict of task:priority
    Returns: updated priority_levels
    """
    priority_levels[task] = "HIGH"
    return priority_levels
