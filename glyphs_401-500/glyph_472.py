# glyph_472 – DATA_PIVOT
# Pivot shared data into a new structure for analysis

def glyph_472(data, pivot_key):
    """
    data: list of dicts
    pivot_key: key to pivot on
    Returns: dict of pivot_value:list_of_records
    """
    pivoted = {}
    for record in data:
        key_val = record.get(pivot_key)
        pivoted.setdefault(key_val, []).append(record)
    return pivoted
