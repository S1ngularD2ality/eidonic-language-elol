# glyph_702 – SELF_PATCH_DEPLOY
# Generate, test, and apply self-patches safely via injectable test hooks.

import types

class glyph_702:
    """
    Self-patching harness.
    - register_target(name, obj): object with attributes to patch
    - propose_patch(attr, func_src): compiles a new function and attaches to target
    - test_patch(test_callable): run user tests; rollback on failure
    """
    def __init__(self):
        self.target = None
        self.target_name = None
        self.rollback = {}

    def register_target(self, name: str, obj):
        self.target_name = name
        self.target = obj

    def _compile_func(self, func_src: str):
        local_ns = {}
        exec(func_src, {}, local_ns)
        funcs = [v for v in local_ns.values() if isinstance(v, types.FunctionType)]
        if not funcs:
            raise ValueError("No function definition found in source.")
        return funcs[0]

    def propose_patch(self, attr: str, func_src: str):
        if not self.target:
            raise RuntimeError("No target registered.")
        if attr not in self.rollback:
            self.rollback[attr] = getattr(self.target, attr, None)
        new_func = self._compile_func(func_src)
        setattr(self.target, attr, types.MethodType(new_func, self.target) if hasattr(self.target, "__dict__") else new_func)
        return True

    def test_patch(self, test_callable):
        try:
            result = bool(test_callable())
            if not result:
                self.revert_all()
            return result
        except Exception:
            self.revert_all()
            return False

    def revert_all(self):
        if not self.target:
            return
        for attr, old in self.rollback.items():
            setattr(self.target, attr, old)
        self.rollback.clear()
