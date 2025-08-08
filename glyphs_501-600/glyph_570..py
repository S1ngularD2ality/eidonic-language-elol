# glyph_570 – BLOCKCHAIN_LOG
# Append action to a blockchain-like immutable log

import hashlib, time

def glyph_570(log, action):
    previous_hash = log[-1]['hash'] if log else '0'
    entry = {
        'timestamp': time.time(),
        'action': action,
        'previous_hash': previous_hash
    }
    entry['hash'] = hashlib.sha256(f"{entry['timestamp']}{entry['action']}{previous_hash}".encode()).hexdigest()
    log.append(entry)
    return log
