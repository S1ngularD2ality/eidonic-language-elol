# glyph_610 – HUMANE_TASK_PRIORITY
# Prioritize tasks that improve human well-being

def glyph_610(tasks):
    return sorted(tasks, key=lambda t: t.get('human_benefit', 0), reverse=True)
