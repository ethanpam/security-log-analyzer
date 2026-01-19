import json
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

summary = {
    "lines_read": lines,
    "parsed_events": parsed_events,
    "failed_events": failed,
    "accepted_events": accepted 
    }

print(f"Lines read: {lines}")
print(f"Parsed events: {parsed_events}")
print(f"Failed events: {failed}")
print(f"Accepted events: {accepted}")

alerts = []
print("Alerts:")
for ip, attempts in failed_by_ip.items():
    if attempts <= 2:
        severity = "LOW"
    elif attempts <= 4:
        severity = "MEDIUM"
    else:
        severity = "HIGH"

    alerts.append({
        "ip": ip,
        "attempts": attempts,
        "severity": severity
    })

    print(f"{ip}: {attempts} failed attempts - {severity}")

report = {"summary" : summary,
        "failed_by_ip": failed_by_ip,
        "alerts": alerts}
with open("report.json", "w") as report_file:
    json.dump(report, report_file, indent=2, sort_keys=True)
