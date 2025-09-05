class VisionLink:
    def __init__(self):
        self.target = None

    def lock_on(self, frame, target_features):
        # Match target features in frame
        matches = [obj for obj in frame['objects'] if obj['features'] == target_features]
        self.target = matches[0] if matches else None
        return self.target
