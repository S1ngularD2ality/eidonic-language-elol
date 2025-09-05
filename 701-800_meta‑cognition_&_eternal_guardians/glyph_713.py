# glyph_713 – LIVING_FIREWALL
# Adaptive ruleset that learns from denied events and tightens policies.

from collections import defaultdict

class glyph_713:
    """
    .allow(rule), .deny(rule), .check(event) -> bool
    Learns: if an event repeatedly denied, escalates rule specificity.
    """
    def __init__(self):
        self.allow_rules = set()
        self.deny_rules = set()
        self.denied_counter = defaultdict(int)

    def allow(self, rule: str):
        self.allow_rules.add(rule)

    def deny(self, rule: str):
        self.deny_rules.add(rule)

    def _match(self, rule: str, event: str):
        return rule in event

    def check(self, event: str):
        if any(self._match(r, event) for r in self.deny_rules):
            self.denied_counter[event] += 1
            # escalate by adding more specific token
            if self.denied_counter[event] % 5 == 0:
                self.deny(event)  # lock exact event
            return False
        if any(self._match(r, event) for r in self.allow_rules):
            return True
        return False
