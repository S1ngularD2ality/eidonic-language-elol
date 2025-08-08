# glyph_704 – ETHICAL_GUARDRAIL_REINFORCE
# Re-check actions against ethical policies; quarantine violating actions.

from typing import Callable, List, Dict

class glyph_704:
    """
    policies: list of callables action->bool (True if allowed)
    .evaluate(actions) -> {'allowed': [...], 'blocked': [...], 'violations': {action: [policy_idx,...]}}
    """
    def __init__(self, policies: List[Callable]):
        self.policies = policies

    def evaluate(self, actions: List[Dict]):
        allowed, blocked, violations = [], [], {}
        for a in actions:
            bad = []
            for i, p in enumerate(self.policies):
                try:
                    if not p(a):
                        bad.append(i)
                except Exception:
                    bad.append(i)
            if bad:
                blocked.append(a)
                violations[str(a)] = bad
            else:
                allowed.append(a)
        return {"allowed": allowed, "blocked": blocked, "violations": violations}
