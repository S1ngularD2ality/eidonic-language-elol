# glyph_766 – AUTONOMOUS_BACKUP_ROTATION
# Rotate backups automatically based on age.

import os
import time

def glyph_766(backup_dir, retention_days=30):
    now = time.time()
    for f in os.listdir(backup_dir):
        path = os.path.join(backup_dir, f)
        if os.path.isfile(path) and (now - os.path.getmtime(path)) > retention_days * 86400:
            os.remove(path)
