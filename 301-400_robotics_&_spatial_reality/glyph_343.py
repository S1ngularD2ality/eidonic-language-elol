# glyph_343 – LIDAR_MERGE
# Fuse data from multiple lidar sources into one comprehensive map

def glyph_343(lidar_arrays):
    """
    lidar_arrays: list of arrays
    Returns: merged array
    """
    import numpy as np
    return np.mean(lidar_arrays, axis=0)
