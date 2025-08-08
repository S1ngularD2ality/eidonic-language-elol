# glyph_791 – AUTONOMOUS_CONTEXT_REPAIR
# Repairs context loss in conversation or processing.

def glyph_791(context, history):
    if not context and history:
        return history[-1]
    return context
