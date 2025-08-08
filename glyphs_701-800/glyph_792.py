# glyph_792 – LIVING_AUDITOR
# Persistent EKRP that records and reviews every decision.

class glyph_792:
    def __init__(self):
        self.records = []

    def log(self, decision):
        self.records.append(decision)

    def review(self):
        return self.records
