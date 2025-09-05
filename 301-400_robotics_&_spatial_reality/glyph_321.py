# glyph_321 – AIRFLOW_SENSE
# Detect and map air movement for navigation in dynamic environments

def glyph_321(air_sensors):
    """
    air_sensors: dict of sensor_id:velocity
    Returns: airflow_map (avg flow vector, anomalies)
    """
    avg_x = sum(v[0] for v in air_sensors.values()) / len(air_sensors)
    avg_y = sum(v[1] for v in air_sensors.values()) / len(air_sensors)
    return {'avg_flow': (avg_x, avg_y), 'sensor_data': air_sensors}
