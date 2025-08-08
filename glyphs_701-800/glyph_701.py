# glyph_701 – REASON_CHAIN_AUDIT
# Continuously audit chains of reasoning for consistency, circularity, and unsupported jumps.

from collections import defaultdict

class glyph_701:
    """
    Track steps in a reasoning chain and flag issues:
      - Missing premises
      - Circular references
      - Contradictions (simple string-based negation check)
    """
    def __init__(self):
        self.steps = []              # list of dict: {"id": str, "claim": str, "supports": [ids]}
        self.index = {}              # id -> step
        self.support_graph = defaultdict(set)  # id -> supporting ids

    def add_step(self, step_id: str, claim: str, supports=None):
        if supports is None:
            supports = []
        step = {"id": step_id, "claim": claim, "supports": supports}
        self.steps.append(step)
        self.index[step_id] = step
        self.support_graph[step_id].update(supports)

    def _detect_missing_premises(self):
        missing = set()
        for s in self.steps:
            for sup in s["supports"]:
                if sup not in self.index:
                    missing.add((s["id"], sup))
        return list(missing)

    def _detect_circular(self):
        visited, stack, cycles = set(), set(), []

        def dfs(n):
            if n in stack:
                cycles.append(n)
                return
            if n in visited:
                return
            visited.add(n)
            stack.add(n)
            for m in self.support_graph.get(n, []):
                dfs(m)
            stack.remove(n)

        for node in self.support_graph:
            dfs(node)
        return list(set(cycles))

    def _detect_contradictions(self):
        # naive contradiction: claim starts with "not " and matches another claim sans "not "
        claims = {}
        for s in self.steps:
            claims[s["id"]] = s["claim"].strip().lower()
        contradictions = []
        for a, ca in claims.items():
            if ca.startswith("not "):
                base = ca[4:].strip()
                for b, cb in claims.items():
                    if b != a and cb == base:
                        contradictions.append((a, b))
        return contradictions

    def audit(self):
        return {
            "missing_premises": self._detect_missing_premises(),
            "circular_references": self._detect_circular(),
            "contradictions": self._detect_contradictions(),
            "step_count": len(self.steps)
        }
