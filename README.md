# FortiGate Log Parser

This Python script is designed to parse FortiGate logs, extract key information from them, and export the data to an Excel file for further analysis. It uses regular expressions to match patterns in the log entries and stores the results in a structured format, which can be easily opened and analyzed in tools like Excel.

## Features
-> Parse FortiGate log files.

-> Extract key information such as timestamps, IP addresses, session details, actions, and more.

-> Export the parsed data to an Excel file for easy analysis.

## Requirements

This script requires Python and the following Python libraries:
`pandas` (for handling and exporting the data to Excel)
`re` (for regular expression pattern matching) -> part of Python's standard library
`argparse` (for handling command-line arguments) -> part of Python's standard library

To install the required dependencies, you can use the following command:

pip install -r requirements.txt

# How to execute (Note: provide file path .log file or keep them in same directriy/path)
  -> python fortigate_log_parser.py -i fortilog.log    (Click Enter <-")
