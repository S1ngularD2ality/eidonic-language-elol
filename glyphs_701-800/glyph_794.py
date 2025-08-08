# glyph_794 – INSTANT_FAILOVER
# Switch to backup system instantly.

def glyph_794(primary_fn, backup_fn, *args, **kwargs):
    try:
        return primary_fn(*args, **kwargs)
    except Exception:
        return backup_fn(*args, **kwargs)
