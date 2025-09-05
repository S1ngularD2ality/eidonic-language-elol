# glyph_765 – RESOURCE_HARMONY_MANAGER
# Balances CPU, memory, and I/O usage across modules.

def glyph_765(resources):
    """
    resources: dict {module: {'cpu':float, 'mem':float, 'io':float}}
    Returns: balanced_resources
    """
    total_cpu = sum(r['cpu'] for r in resources.values())
    total_mem = sum(r['mem'] for r in resources.values())
    total_io = sum(r['io'] for r in resources.values())
    factor = max(total_cpu, total_mem, total_io) or 1
    return {m: {k: v/factor for k, v in vals.items()} for m, vals in resources.items()}
