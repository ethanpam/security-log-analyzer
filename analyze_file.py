from parser import parser

lines = 0
parsed_events = 0
failed = 0
accepted = 0
failed_by_ip = {}

with open("sample_auth.log") as f:
    for row in f:
        row = row.strip()
        lines += 1

        if not row:
            continue

        parsed_row = parser(row)
        parsed_events += 1
        
        if parsed_row["event_type"] == "failed":
            failed += 1 
            ip = parsed_row["ip_address"]
            failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1
        elif parsed_row["event_type"] == "accepted":
            accepted += 1

print(f"Lines read: {lines}")
print(f"Parsed events: {parsed_events}")
print(f"Failed events: {failed}")
print(f"Accepted events: {accepted}")

print(f"Failed attempts by IP:")
for ip, attempt in failed_by_ip.items():
    print(f"{ip}: {attempt}")