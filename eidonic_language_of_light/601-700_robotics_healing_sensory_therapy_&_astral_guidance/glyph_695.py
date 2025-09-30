# glyph_695.py — DREAM_STATE_MONITOR
# -----------------------------------------------------------------------------
# ID:            695
# Pack:          Pack 007 (601–700)
# Name:          DREAM_STATE_MONITOR
# Class:         guidance.journal
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List

def glyph_695(events: List[Dict]) -> Dict:
    """
    DREAM_STATE_MONITOR — normalize dream log entries for later reflection.

    Overview
    --------
    Standardizes timestamped notes with tags; emits stats for recall and themes.

    Parameters
    ----------
    events : List[Dict]
        Each: {"t": epoch/seconds, "tags": ["symbol","feeling"], "note": "text"}

    Returns
    -------
    Dict
        Journal model with theme frequencies.
    """
    log = [{"t": float(e["t"]), "tags": list(e.get("tags", [])), "note": str(e.get("note",""))} for e in events]
    # frequency of tags
    freq = {}
    for e in log:
        for tag in e["tags"]:
            freq[tag] = freq.get(tag, 0) + 1
    return {"type":"dream_monitor","entries":sorted(log, key=lambda e: e["t"]),"tag_freq":freq}
