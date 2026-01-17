# Security Log Analyzer
A Python-based tool that analyzes Linux authentication logs to detect suspicious SSH login activity.

This project was built to help me learn cybersecurity concepts such as log parsing, failed authentication detection, and basic incident analysis.


## Features

- Parses Linux authentication log entries (`auth.log`-style)
- Extracts key fields:
  - Timestamp
  - Event type (failed / accepted)
  - Username
  - IP address
- Reads a saved log file and reports:
  - Total lines read
  - Parsed authentication events
  - Failed login count
  - Accepted login count
- Includes unit tests using `pytest`


## Project Structure

security-log-analyzer/
├── parser.py # Parses individual authentication log lines
├── analyze_file.py # Reads a log file and summarizes events
├── sample_auth.log # Sample authentication log for testing
├── test_parser.py # Unit tests for the parser
├── .gitignore
├── LICENSE
└── README.md


## How to Run

### Analyze the sample log file

```bash
python analyze_file.py
```

### Run tests

```bash
pytest test_parser.py
```


## Learning Goals

- This project is designed to help learn:
  - How Linux authentication logs work
  - How SSH login attempts are recorded
  - How brute-force behavior appears in logs
  - How to extract structured security data from raw text
  - How basic security monitoring tools are built


## Roadmap

- Planned improvements:
  - Count failed login attempts per IP address
  - Detect brute-force behavior using thresholds
  - Assign severity levels (low / medium / high)
  - Generate summary reports for basic incident triage


## License

[MIT](https://choosealicense.com/licenses/mit/)
