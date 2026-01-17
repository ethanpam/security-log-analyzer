from parser import parser

lines = 0
parsed_events = 0
failed = 0
accepted = 0

with open("sample_auth.log") as f:
    for row in f:
        row = row.strip()
        lines += 1

        if not row:
            continue

        parsered_row = parser(row)
        parsed_events += 1
        
        if parsered_row["event_type"] == "failed":
            failed += 1
        elif parsered_row["event_type"] == "accepted":
            accepted += 1

print(f"Lines read: {lines}")
print(f"Parsed events: {parsed_events}")
print(f"Failed events: {failed}")
print(f"Accepted events: {accepted}")

