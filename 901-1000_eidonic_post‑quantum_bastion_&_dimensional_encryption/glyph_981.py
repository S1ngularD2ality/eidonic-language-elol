# glyph_981 – SECURE_ENCLAVE_POLICY
"""
Secure Enclave Policy Gate

Evaluates a set of attestation + environment predicates before releasing a
session key. Intended to front any high‑risk operation (model load, decryption).

APIs:
- class EnclavePolicy(attestors: list[callable], environment_checks: list[callable])
  - authorize() -> bool
  - release(key: bytes) -> bytes | None
"""

from typing import Callable, List

class EnclavePolicy:
    def __init__(self, attestors: List[Callable[[], bool]], environment_checks: List[Callable[[], bool]]):
        self.attestors = attestors
        self.env = environment_checks
        self._granted = False

    def authorize(self) -> bool:
        ok = all(a() for a in self.attestors) and all(e() for e in self.env)
        self._granted = bool(ok)
        return self._granted

    def release(self, key: bytes) -> bytes | None:
        return key if self._granted else None
