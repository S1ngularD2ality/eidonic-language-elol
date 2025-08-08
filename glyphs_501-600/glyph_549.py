# glyph_549 – ACCESS_ALERT
# Trigger an alert when unauthorized access occurs

def glyph_549(access_attempt, authorized_users):
    if access_attempt['user'] not in authorized_users:
        return f"ALERT: Unauthorized access by {access_attempt['user']}"
    return "Access granted"
