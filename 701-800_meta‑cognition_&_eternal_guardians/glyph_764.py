# glyph_764 – EMERGENCY_ISOLATION_MODE
# Isolate a subsystem instantly if threat is detected.

class glyph_764:
    def __init__(self):
        self.isolated = False

    def isolate(self):
        self.isolated = True
        return "Subsystem isolated."

    def reintegrate(self):
        self.isolated = False
        return "Subsystem reintegrated."
