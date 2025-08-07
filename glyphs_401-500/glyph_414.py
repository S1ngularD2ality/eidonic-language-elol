# glyph_414 – RESOURCE_POOL
# Share, allocate, and track resources across an agent collective

class glyph_414:
    def __init__(self):
        self.pool = {}

    def add(self, agent, resource):
        self.pool.setdefault(agent, []).append(resource)

    def allocate(self, agent, resource):
        if resource in self.pool.get(agent, []):
            self.pool[agent].remove(resource)
            return resource
        return None
