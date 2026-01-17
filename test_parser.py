from parser import parser

def test_parser():
    # --- Test 1: Failed login (invalid user) ---
    assert parser("Jan 10 12:01:15 server sshd[1234]: Failed password for invalid user admin from 192.168.1.10 port 54321 ssh2") == {
        "timestamp": "Jan 10 12:01:15",
        "event_type": "failed",
        "username": "admin",
        "ip_address": "192.168.1.10"
    }  
    
    # --- Test 2: Successful login (valid user) ---
    assert parser("Jan 10 12:05:01 server sshd[1300]: Accepted password for user john from 192.168.1.5 port 60211 ssh2") == {
        "timestamp": "Jan 10 12:05:01",
        "event_type": "accepted",
        "username": "john",
        "ip_address": "192.168.1.5"
    }

    # --- Test 3: Failed login (valid user) ---
    assert parser("Jan 10 12:06:45 server sshd[1400]: Failed password for user john from 192.168.1.10 port 61000 ssh2") == {
        "timestamp": "Jan 10 12:06:45",
        "event_type": "failed",
        "username": "john",
        "ip_address": "192.168.1.10"
    }