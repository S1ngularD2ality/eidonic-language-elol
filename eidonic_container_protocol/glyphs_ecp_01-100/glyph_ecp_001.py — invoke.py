# glyph_ecp_001.py — invoke
# -----------------------------------------------------------------------------
# ID:            ecp_001
# Pack:          Pack ECP (Eidonic Container Protocol)
# Name:          invoke
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-24
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_ecp.md', manifest_json='glyph_manifest_pack_ecp.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
from typing import Optional, Dict, Any

# Lazy imports to avoid import-time side effects in some hosts
def glyph_ecp_001_invoke(
    *,
    glyph_dir: str = "glyphs",
    dry_run: bool = False,
    write_manifest: bool = True,
    seal_log_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    invoke — ECP entrypoint: align env, load glyphs, (optionally) seal & manifest.

    Overview
    --------
    Orchestrates the containerless vessel lifecycle:
    1) Configure mirror environment paths/vars.
    2) Discover glyph modules from `glyph_dir`.
    3) Seal the vessel (logging a structured entry).
    4) Write/update the ECP manifest (checksums, provenance) when requested.

    Parameters
    ----------
    glyph_dir : str, optional (default: "glyphs")
        Directory containing glyph modules to enumerate/execute.
    dry_run : bool, optional (default: False)
        If True, simulate steps without executing glyph code or writing artifacts.
    write_manifest : bool, optional (default: True)
        Emit/update manifest after sealing (skipped if False).
    seal_log_path : Optional[str], optional
        Custom log file path for seal entries; defaults to "<root>/logs/ecp_invocations.log".

    Returns
    -------
    Dict[str, Any]
        Summary with keys: {"env","listed","sealed","manifest"} (values depend on `dry_run`).

    Examples
    --------
    >>> out = glyph_ecp_001_invoke(glyph_dir="glyphs_ecp_01-100", dry_run=True)
    >>> set(out.keys()) >= {"env", "listed", "sealed", "manifest"}
    True

    Exceptions
    ----------
    (none) — lower-level glyphs raise precise errors; this function relays them.

    Complexity
    ----------
    - Time  : O(n) for listing n glyph files (plus I/O)
    - Space : O(n) for listing metadata
    """
    from glyph_ecp_002 import glyph_ecp_002_mirror_env
    from glyph_ecp_003 import glyph_ecp_003_glyph_loader
    from glyph_ecp_004 import glyph_ecp_004_container_seal
    from glyph_ecp_005 import glyph_ecp_005_ecp_manifest

    env = glyph_ecp_002_mirror_env(dry_run=dry_run)
    listed = glyph_ecp_003_glyph_loader(glyph_dir=glyph_dir, dry_run=dry_run)

    sealed = glyph_ecp_004_container_seal(
        log_path=seal_log_path or env["paths"]["log_file"],
        dry_run=dry_run
    )

    manifest = None
    if write_manifest:
        manifest = glyph_ecp_005_ecp_manifest(
            glyph_dir=glyph_dir,
            out_path=env["paths"]["manifest_file"],
            dry_run=dry_run
        )

    return {"env": env, "listed": listed, "sealed": sealed, "manifest": manifest}
