# glyph_706 – ERROR_PATTERNS_DETECT
# Mine error logs to discover repeating patterns and frequencies.

from collections import Counter
import re

def glyph_706(log_lines, regex=r"(ERROR|WARN):\s*(.+)"):
    """
    Returns: list of (pattern, count) sorted by count desc.
    """
    bucket = Counter()
    for line in log_lines:
        m = re.search(regex, line)
        if m:
            bucket[m.group(2).strip()] += 1
    return bucket.most_common()
