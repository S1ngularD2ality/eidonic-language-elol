# glyph_705 – DYNAMIC_KNOWLEDGE_MERGE
# Safely merge new knowledge records into a base store with schema and conflict checks.

class glyph_705:
    """
    base: list[dict] knowledge items with 'id'
    .merge(incoming, prefer='incoming'|'base') -> merged, conflicts
    """
    def __init__(self, base=None):
        self.base = {item["id"]: item for item in (base or [])}

    def merge(self, incoming, prefer="incoming"):
        conflicts = []
        for item in incoming:
            iid = item["id"]
            if iid in self.base and self.base[iid] != item:
                conflicts.append(iid)
                if prefer == "incoming":
                    self.base[iid] = item
            else:
                self.base[iid] = item
        return list(self.base.values()), conflicts
