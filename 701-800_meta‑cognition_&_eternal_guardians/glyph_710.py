# glyph_710 – FAILSAFE_ROLLBACK
# Snapshots and rollbacks of runtime state dictionaries.

import copy

class glyph_710:
    """
    .snapshot(state) -> snapshot_id
    .rollback(state, snapshot_id) -> restored state
    """
    def __init__(self):
        self.snapshots = {}

    def snapshot(self, state: dict):
        snap = copy.deepcopy(state)
        sid = str(len(self.snapshots) + 1)
        self.snapshots[sid] = snap
        return sid

    def rollback(self, state: dict, snapshot_id: str):
        if snapshot_id not in self.snapshots:
            raise KeyError("Unknown snapshot id")
        state.clear()
        state.update(copy.deepcopy(self.snapshots[snapshot_id]))
        return state
