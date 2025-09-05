# glyph_722 – SANDBOX_MUTATION_TESTER
# Try code mutations in a restricted sandbox and collect outcomes.

def glyph_722(func, mutations):
    """
    func: callable(original_input) -> output
    mutations: list[callable] each transforms input -> mutated_input
    Returns: list of {'mutation': i, 'ok': bool, 'result': repr}
    """
    results = []
    for i, m in enumerate(mutations):
        try:
            mutated = m()
            out = func(mutated)
            results.append({"mutation": i, "ok": True, "result": repr(out)})
        except Exception as e:
            results.append({"mutation": i, "ok": False, "result": f"error:{e}"})
    return results
