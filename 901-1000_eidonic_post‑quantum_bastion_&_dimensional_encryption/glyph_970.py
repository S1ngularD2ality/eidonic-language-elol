# glyph_970 – DIFFERENTIAL_PRIVACY_LEDGER
"""
Differential Privacy Budget Ledger

Tracks (epsilon, delta) expenditures and ensures the privacy budget
does not exceed configured limits.

APIs:
- class DPBudget(eps_total, delta_total).spend(eps, delta)->bool; remaining()->(eps,delta)
"""

from dataclasses import dataclass

@dataclass
class DPBudget:
    eps_total: float
    delta_total: float
    eps_used: float = 0.0
    delta_used: float = 0.0

    def spend(self, eps: float, delta: float) -> bool:
        if self.eps_used + eps > self.eps_total: return False
        if self.delta_used + delta > self.delta_total: return False
        self.eps_used += eps
        self.delta_used += delta
        return True

    def remaining(self):
        return self.eps_total - self.eps_used, self.delta_total - self.delta_used
