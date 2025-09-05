# glyph_723 – SELF_REGRESSION_SUITE
# Maintain a small registry of assertions and run them as regression tests.

class glyph_723:
    def __init__(self):
        self.tests = []  # list of callables returning True/False

    def add(self, test_callable):
        self.tests.append(test_callable)

    def run(self):
        passed, failed = [], []
        for i, t in enumerate(self.tests):
            try:
                (passed if t() else failed).append(i)
            except Exception:
                failed.append(i)
        return {"passed": passed, "failed": failed, "total": len(self.tests)}
