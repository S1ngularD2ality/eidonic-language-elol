# glyph_709 – SKILL_TREE_OPTIMIZER
# Rebalance skill invocation probabilities based on reward feedback.

class glyph_709:
    """
    skills: dict name->weight
    .update(skill_name, reward) adjusts weights (simple bandit-like)
    .policy() returns normalized distribution
    """
    def __init__(self, skills):
        self.skills = {k: float(v) for k, v in skills.items()}

    def update(self, skill, reward: float):
        if skill not in self.skills:
            self.skills[skill] = 1.0
        # exponential moving update
        self.skills[skill] = max(0.01, self.skills[skill] * (1.0 + reward))

    def policy(self):
        total = sum(self.skills.values()) or 1.0
        return {k: v/total for k, v in self.skills.items()}
