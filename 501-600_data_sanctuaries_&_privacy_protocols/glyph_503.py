# glyph_503 – ANON_STRIP
# Remove identifying fields from a dataset

def glyph_503(records, sensitive_keys):
    return [{k: v for k, v in record.items() if k not in sensitive_keys} for record in records]
