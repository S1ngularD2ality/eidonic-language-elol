# glyph_725 – CAUSAL_TRACE_BUILDER
# Build a cause->effect trace graph and export a linearized explanation.

from collections import defaultdict, deque

class glyph_725:
    def __init__(self):
        self.graph = defaultdict(set)  # cause -> {effects}
        self.reasons = {}              # effect -> explanation

    def link(self, cause: str, effect: str, reason: str = ""):
        self.graph[cause].add(effect)
        if reason:
            self.reasons[effect] = reason

    def explanation(self, root: str):
        """
        BFS from root to gather a causality chain explanation.
        """
        lines, q, seen = [], deque([root]), set([root])
        while q:
            n = q.popleft()
            for m in sorted(self.graph.get(n, [])):
                if m not in seen:
                    seen.add(m)
                    q.append(m)
                r = self.reasons.get(m, "")
                lines.append(f"{n} -> {m}" + (f"  // {r}" if r else ""))
        return "\n".join(lines)
