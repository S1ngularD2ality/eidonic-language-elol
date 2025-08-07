class ObjectSoul:
    def __init__(self):
        self.objects = {}

    def track(self, detections):
        for det in detections:
            obj_id = hash(str(det['features']))
            self.objects[obj_id] = det
        return list(self.objects.keys())
