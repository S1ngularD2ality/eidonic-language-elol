# glyph_740 – INCIDENT_POSTMORTEM
# Aggregate logs, metrics, and timeline into a concise incident report.

import time

class glyph_740:
    def __init__(self):
        self.events = []  # list of (ts, kind, payload)

    def log(self, kind: str, payload: str):
        self.events.append((time.time(), kind, payload))

    def report(self):
        if not self.events:
            return "# Incident Report\n\nNo events recorded."
        start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.events[0][0]))
        end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.events[-1][0]))
        lines = [f"# Incident Report", f"**Window:** {start} — {end}", ""]
        kinds = {}
        for ts, kind, payload in self.events:
            kinds.setdefault(kind, 0)
            kinds[kind] += 1
            ts_s = time.strftime("%H:%M:%S", time.localtime(ts))
            lines.append(f"- [{ts_s}] **{kind}** — {payload}")
        lines.append("\n## Summary by Type")
        for k, c in kinds.items():
            lines.append(f"- {k}: {c} events")
        return "\n".join(lines)
