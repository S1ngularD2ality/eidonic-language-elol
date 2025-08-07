# glyph_383 – POWER_BALANCE
# Monitor and balance internal power distribution

class glyph_383:
    def __init__(self, sources):
        self.sources = sources

    def balance(self):
        total = sum(self.sources.values())
        avg = total / len(self.sources)
        for k in self.sources:
            self.sources[k] = avg
        return self.sources
