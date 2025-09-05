# glyph_960 – RED_TEAM_SANDBOX_GUARD
"""
Red-Team Sandbox Guard

Executes provided actions only when all safety predicates pass
(e.g., running inside a sandbox VM, no outbound net, write-locked FS).
Prevents dangerous ops from escaping controlled environments.

APIs:
- guard_execute(action: callable, predicates: List[callable])-> (ok, result|err)
"""

from typing import Callable, List, Tuple

def guard_execute(action: Callable[[], object], predicates: List[Callable[[], bool]]) -> Tuple[bool, object]:
    if not all(p() for p in predicates):
        return False, "Denied: sandbox predicates not satisfied."
    try:
        return True, action()
    except Exception as e:
        return False, f"Execution error: {e}"
