# glyph_996 – AGENT_BEHAVIOR_SANDBOX
"""
Agent Behavior Sandbox

Evaluates proposed agent actions against a policy (allow/deny + reason).
Use to prevent unbounded code exec, network exfil, or file writes.

APIs:
- class Sandbox(policy: dict).check(action: dict)->(bool, str)
"""

class Sandbox:
    def __init__(self, policy: dict):
        self.policy = policy

    def check(self, action: dict) -> tuple[bool, str]:
        kind = action.get("kind")
        if kind in self.policy.get("deny_kinds", []):
            return False, f"Denied kind: {kind}"
        # Network guard
        if kind == "net" and not self.policy.get("allow_network", False):
            return False, "Network disabled"
        # Path guard
        path = action.get("path", "")
        for p in self.policy.get("deny_paths", []):
            if path.startswith(p):
                return False, f"Denied path: {p}"
        return True, "OK"
