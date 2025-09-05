# glyph_632 – GENTLE_AIRFLOW_CONTROL
# Adjust airflow to avoid disturbing fragile objects or papers

def glyph_632(current_airflow, fragility_level):
    return max(0.1, current_airflow * (1 - fragility_level))
