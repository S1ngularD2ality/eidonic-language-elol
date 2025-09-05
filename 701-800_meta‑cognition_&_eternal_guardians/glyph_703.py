# glyph_703 – EKRP_LIFEGUARD
# Persistent EKRP that watches other agents for stall, drift, and anomaly signals.

import time

class glyph_703:
    """
    Lifeguard monitors heartbeats, drift metrics, and error counts.
    Use .heartbeat(agent) periodically; call .report() for status.
    """
    def __init__(self, stall_secs=10, drift_threshold=0.3, error_threshold=3):
        self.last_seen = {}         # agent -> timestamp
        self.drift = {}             # agent -> float
        self.errors = {}            # agent -> int
        self.cfg = {"stall_secs": stall_secs, "drift_threshold": drift_threshold, "error_threshold": error_threshold}

    def heartbeat(self, agent: str, drift: float = 0.0, error_increment: int = 0):
        self.last_seen[agent] = time.time()
        self.drift[agent] = max(self.drift.get(agent, 0.0), drift)
        if error_increment:
            self.errors[agent] = self.errors.get(agent, 0) + error_increment

    def _stalled(self, agent):
        return (time.time() - self.last_seen.get(agent, 0)) > self.cfg["stall_secs"]

    def report(self):
        flags = {}
        for agent in set(list(self.last_seen) + list(self.drift) + list(self.errors)):
            issues = []
            if self._stalled(agent):
                issues.append("stall")
            if self.drift.get(agent, 0) >= self.cfg["drift_threshold"]:
                issues.append("drift")
            if self.errors.get(agent, 0) >= self.cfg["error_threshold"]:
                issues.append("errors")
            flags[agent] = issues
        return flags
