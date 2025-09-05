class GraspingHand:
    def __init__(self):
        self.grip_force = 0

    def adapt_grip(self, object_weight, fragility):
        base_force = object_weight * 1.5
        if fragility > 0.8:
            self.grip_force = min(base_force, 5)
        else:
            self.grip_force = min(base_force, 15)
        return self.grip_force
