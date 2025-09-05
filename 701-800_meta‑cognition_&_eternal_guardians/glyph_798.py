# glyph_798 – WATCHER_NETWORK
# Distributed watcher EKRPs communicating continuously.

class glyph_798:
    def __init__(self):
        self.watchers = []

    def add_watcher(self, watcher_fn):
        self.watchers.append(watcher_fn)

    def poll(self):
        return [w() for w in self.watchers]
