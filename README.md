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
- Aggregates failed login attempts by IP address
- Assigns severity levels based on thresholds:
  - 🟢 LOW (1–2 failed attempts)
  - 🟡 MEDIUM (3–4 failed attempts)
  - 🔴 HIGH (5+ failed attempts)
- Prints human-readable alerts to the terminal
- Generates a structured JSON report (`report.json`) for basic incident triage
- Includes unit tests using `pytest`


## Project Structure
```text
security-log-analyzer/
├── parser.py # Parses individual authentication log lines
├── analyze_file.py # Reads a log file and summarizes events
├── sample_auth.log # Sample authentication log for testing
├── test_parser.py # Unit tests for the parser
├── .gitignore
├── LICENSE
└── README.md
```

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

- This project is designed to help me learn:
  - How Linux authentication logs work
  - How SSH login attempts are recorded
  - How brute-force behavior appears in logs
  - How to extract structured security data from raw text
  - How basic security monitoring tools are built

## Test Data Disclaimer

- The `sample_auth.log` file used for testing was generated using AI-assisted tools to resemble realistic Linux authentication logs.
  - No real users, systems, or productions logs were used
  - No real credentials or sensitive data are included
  - The data is inteneded solely for development and demostration purposes

## License

[MIT](https://choosealicense.com/licenses/mit/)
