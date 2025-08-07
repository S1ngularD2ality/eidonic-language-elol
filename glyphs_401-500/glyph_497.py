# glyph_497 – TASK_TIMEOUT
# Set a timeout for task completion

def glyph_497(task, timeout_seconds):
    """
    task: callable
    timeout_seconds: int
    Returns: task result or 'timeout'
    """
    import threading

    result = ["timeout"]

    def wrapper():
        result[0] = task()

    t = threading.Thread(target=wrapper)
    t.start()
    t.join(timeout_seconds)
    return result[0]
