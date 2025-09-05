# glyph_767 – SYSTEM_LATENCY_ANALYZER
# Analyze and report system latency patterns.

import statistics

def glyph_767(latencies):
    return {
        "avg": statistics.mean(latencies),
        "max": max(latencies),
        "min": min(latencies)
    }
