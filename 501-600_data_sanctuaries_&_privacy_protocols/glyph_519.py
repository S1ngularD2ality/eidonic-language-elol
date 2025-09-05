# glyph_519 – ACCESS_LOGGER
# Log data access with timestamp

import time

def glyph_519(user, resource, log):
    log.append({'user': user, 'resource': resource, 'time': time.time()})
    return log
