# glyph_361 – DUAL_MODE
# Seamless switching between autonomous and teleoperated control

class glyph_361:
    def __init__(self):
        self.mode = "autonomous"

    def switch(self):
        self.mode = "teleop" if self.mode == "autonomous" else "autonomous"
        return self.mode
