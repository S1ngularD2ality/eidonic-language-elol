# glyph_542 – INTRUSION_PATTERN
# Detect patterns of repeated failed access attempts

def glyph_542(logs, fail_threshold=5):
    ip_attempts = {}
    for log in logs:
        ip_attempts[log['ip']] = ip_attempts.get(log['ip'], 0) + (1 if log['status'] == 'fail' else 0)
    return [ip for ip, fails in ip_attempts.items() if fails >= fail_threshold]
