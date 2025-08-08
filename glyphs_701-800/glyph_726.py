# glyph_726 – CONSTRAINT_SOLVER
# Simple backtracking solver for finite-domain constraints.

def glyph_726(variables, domains, constraints):
    """
    variables: list[str]
    domains: dict[str, list[any]]
    constraints: list[callable(assignments)->bool] checked on partial assignments
    Returns: a satisfying assignment dict or None
    """
    assignment = {}

    def consistent(assign):
        return all(c(assign) for c in constraints)

    def backtrack(i=0):
        if i == len(variables):
            return dict(assignment)
        var = variables[i]
        for val in domains[var]:
            assignment[var] = val
            if consistent(assignment):
                sol = backtrack(i + 1)
                if sol is not None:
                    return sol
        assignment.pop(var, None)
        return None

    return backtrack()
