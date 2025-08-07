# glyph_315 – FORCE_FEEDBACK
# Sense and respond to pressure/force on robotic actuators

class glyph_315:
    def __init__(self, sensitivity=1.0):
        self.force = 0
        self.sensitivity = sensitivity

    def update(self, force_reading):
        self.force = force_reading * self.sensitivity
        return self.force
