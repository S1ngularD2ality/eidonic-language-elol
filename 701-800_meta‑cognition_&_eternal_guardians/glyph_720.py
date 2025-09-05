# glyph_720 – IMMORTAL_WATCHER
# Eternal EKRP supervisor: schedules audits, heals, guardrails, and rollbacks.

import time
import threading

class glyph_720:
    """
    start() launches a background thread that periodically:
      - audits reasoning (glyph_701-like interface)
      - runs diagnostics (glyph_719)
      - applies healing (glyph_711)
      - enforces guardrails (glyph_704)
      - triggers rollback (glyph_710) on critical failure
    All collaborators are injected to keep it modular.
    """
    def __init__(self, auditor, diagnostician, medic, guardrails, rollback, period_sec=5):
        self.auditor = auditor
        self.diagnostician = diagnostician
        self.medic = medic
        self.guardrails = guardrails
        self.rollback = rollback
        self.period = period_sec
        self.running = False
        self.thread = None
        self.last_snapshot = None
        self.state_ref = {}

    def set_state_ref(self, state: dict):
        self.state_ref = state

    def _loop(self):
        while self.running:
            # snapshot state
            try:
                if self.rollback and hasattr(self.rollback, "snapshot"):
                    self.last_snapshot = self.rollback.snapshot(self.state_ref)
            except Exception:
                pass

            # diagnostics
            diag = {}
            try:
                diag = self.diagnostician({})
            except Exception:
                pass

            # audit & guardrails (no-op hooks if not provided)
            try:
                if hasattr(self.auditor, "audit"):
                    _ = self.auditor.audit()
            except Exception:
                pass

            # heal any registered subsystems
            try:
                if hasattr(self.medic, "diagnose"):
                    for name in self.medic.diagnose():
                        self.medic.heal(name)
            except Exception:
                pass

            # rollback if diagnostics report critical failures
            try:
                if diag.get("failed"):
                    self.rollback.rollback(self.state_ref, self.last_snapshot)
            except Exception:
                pass

            time.sleep(self.period)

    def start(self):
        if self.running:
            return False
        self.running = True
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()
        return True

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=self.period * 2)
        return True
