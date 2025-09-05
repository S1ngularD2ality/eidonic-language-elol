# glyph_987 – SECURE_CHANNEL_NEGOTIATOR
"""
Secure Channel Negotiator

Picks a cipher suite from capability sets under a policy (no-legacy, PQ-friendly).
Returns selected tuple (kdf, aead, hash) as strings for orchestration.

APIs:
- negotiate(local_caps: set[str], remote_caps: set[str], policy: dict) -> tuple[str,str,str] | None
"""

def negotiate(local_caps: set[str], remote_caps: set[str], policy: dict) -> tuple[str,str,str] | None:
    suites = [
        ("hkdf-blake2b", "aead-siv-blake2b", "blake2b"),
        ("hkdf-sha512",  "aead-siv-blake2b", "sha512"),
    ]
    if policy.get("require_pq_like"):
        suites = [s for s in suites if "blake2b" in s]  # toy filter
    common = []
    for kdf, aead, h in suites:
        if {kdf, aead, h}.issubset(local_caps) and {kdf, aead, h}.issubset(remote_caps):
            common.append((kdf, aead, h))
    return common[0] if common else None
