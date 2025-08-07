class BodyRoot:
    def __init__(self, joint_limits):
        self.joints = {k: 0 for k in joint_limits}
        self.limits = joint_limits

    def update(self, joint_name, angle):
        if self.limits[joint_name][0] <= angle <= self.limits[joint_name][1]:
            self.joints[joint_name] = angle
        else:
            raise ValueError("Angle out of range")
