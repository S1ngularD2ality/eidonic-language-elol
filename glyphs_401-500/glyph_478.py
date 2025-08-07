# glyph_478 – INTERLOCK
# Create dependencies between tasks so one cannot start until another finishes

def glyph_478(tasks, dependencies):
    """
    tasks: dict of task:callable
    dependencies: dict of task:[prerequisites]
    Returns: ordered execution results
    """
    results = {}
    for task, func in tasks.items():
        if all(dep in results for dep in dependencies.get(task, [])):
            results[task] = func()
    return results
