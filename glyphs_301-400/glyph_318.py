# glyph_318 – VOXEL_MAPPER
# Convert sensor data to a 3D voxel grid for spatial analysis

def glyph_318(sensor_points):
    """
    sensor_points: list of (x, y, z) tuples
    Returns: 3D voxel grid (dict or array)
    """
    voxel_grid = {}
    for pt in sensor_points:
        key = (round(pt[0]), round(pt[1]), round(pt[2]))
        voxel_grid[key] = True
    return voxel_grid
