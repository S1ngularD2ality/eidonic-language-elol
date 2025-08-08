# glyph_733 – DATASET_SHIFT_SCANNER
# Compare population statistics between reference and new data.

def glyph_733(ref_stats: dict, new_stats: dict, tolerances: dict):
    """
    stats format: {'feature': {'mean':float,'std':float}}
    tolerances: {'mean':ratio,'std':ratio} allowed new/ref ratios
    Returns: dict feature->['mean','std'] that violate tolerances
    """
    violations = {}
    for feat, r in ref_stats.items():
        n = new_stats.get(feat, {})
        bad = []
        for key in ("mean", "std"):
            rv = max(1e-9, float(r.get(key, 1.0)))
            nv = float(n.get(key, rv))
            if nv / rv > tolerances.get(key, 1.5):
                bad.append(key)
        if bad:
            violations[feat] = bad
    return violations
