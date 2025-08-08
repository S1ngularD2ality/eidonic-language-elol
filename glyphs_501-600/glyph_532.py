# glyph_532 – AUTH_LOG
# Record authentication attempts

import time

def glyph_532(user, status, log):
    log.append({"user": user, "status": status, "time": time.time()})
    return log
