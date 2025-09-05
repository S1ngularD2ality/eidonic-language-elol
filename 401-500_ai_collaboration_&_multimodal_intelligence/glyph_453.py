# glyph_453 – CONTEXT_THREAD
# Maintain a shared context thread for multi-agent projects

class glyph_453:
    def __init__(self):
        self.thread = []

    def add_context(self, context):
        self.thread.append(context)

    def get_context(self):
        return self.thread
