# glyph_608 – OBSTACLE_MEMORY
# Remember location of obstacles to avoid in future missions

def glyph_608(memory, new_obstacles):
    memory.update(new_obstacles)
    return memory
