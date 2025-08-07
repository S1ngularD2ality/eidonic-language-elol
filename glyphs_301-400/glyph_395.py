# glyph_395 – RESOURCE_MAP
# Map and update resource locations (charging, water, tools) for all agents

class glyph_395:
    def __init__(self):
        self.resources = {}

    def update(self, resource_type, position):
        self.resources[resource_type] = position

    def get_location(self, resource_type):
        return self.resources.get(resource_type, None)
