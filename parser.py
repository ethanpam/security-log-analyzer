def parser(logline: str) -> dict:
    ''' Parse one auth line into key fields.
    
    Returns a dict with: timestamp, event_type, username, ip_address
    '''
    tokens = logline.split()

    timestamp = ' '.join(tokens[:3])
    
    event_type = None
    if "Failed password" in logline:
            event_type = "failed"
    elif "Accepted password" in logline:
            event_type = "accepted"
    
    username = None
    ip_address = None

    for i, tok in enumerate(tokens):
        if tok == "user":
            username = tokens[i + 1]
        if tok == "from":
            ip_address = tokens[i + 1]
    
    return {
        "timestamp": timestamp,
        "event_type": event_type,
        "username": username,
        "ip_address": ip_address
    }