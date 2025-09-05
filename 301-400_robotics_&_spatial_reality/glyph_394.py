# glyph_394 – ALERT_CHAIN
# Relay an alert or signal through a mesh of robots or devices

def glyph_394(node_id, alert_message, mesh):
    """
    node_id: current node identifier
    alert_message: message to send
    mesh: dict of node:neighbors
    Returns: list of nodes alerted
    """
    alerted = [node_id]
    for neighbor in mesh.get(node_id, []):
        alerted.append(neighbor)
    return list(set(alerted))
