# glyph_711 – EKRP_MEDIC
# Living EKRP that diagnoses and applies healing procedures to subsystems.

class glyph_711:
    """
    registry: dict name-> {'health':0..1, 'errors':int}
    .diagnose() -> list of issues
    .heal(name) -> applies stepwise healing improving health, reducing errors
    """
    def __init__(self):
        self.registry = {}

    def register(self, name, health=1.0, errors=0):
        self.registry[name] = {"health": float(health), "errors": int(errors)}

    def diagnose(self):
        return {k: v for k, v in self.registry.items() if v["health"] < 0.8 or v["errors"] > 0}

    def heal(self, name):
        if name not in self.registry:
            return None
        r = self.registry[name]
        r["health"] = min(1.0, r["health"] + 0.1)
        r["errors"] = max(0, r["errors"] - 1)
        return r
