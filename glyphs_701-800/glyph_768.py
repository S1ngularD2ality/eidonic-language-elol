# glyph_768 – PREDICTIVE_FAILURE_ALERT
# Predict likely failure based on historical trend.

import statistics

def glyph_768(failure_counts):
    if len(failure_counts) < 3:
        return False
    avg_growth = statistics.mean(failure_counts[i+1] - failure_counts[i] for i in range(len(failure_counts)-1))
    return avg_growth > 0
