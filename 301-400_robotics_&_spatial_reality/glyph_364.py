# glyph_364 – FORCE_FIELD
# Activate and manage a virtual or physical perimeter around the robot

class glyph_364:
    def __init__(self, radius=1.0):
        self.radius = radius

    def is_intruded(self, position, intruders):
        for i in intruders:
            dist = ((position[0] - i[0])**2 + (position[1] - i[1])**2)**0.5
            if dist < self.radius:
                return True
        return False
