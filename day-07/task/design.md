# Design: Log Analyzer (Day 04 / Day 05)

## What problem am I solving?

- Need to quickly see how many INFO, WARNING, and ERROR lines are in an application log.
- Manual counting is slow and error-prone for large logs.
- Script automates counting and gives a summary.

## What input does my script need?

- **Log file path** – path to the application log (e.g. `app.log`).
- Log lines should contain words like `INFO`, `WARNING`, or `ERROR` (e.g. with spaces around them).

## What output should my script give?

- **Terminal**: A short summary with counts, e.g.:
  - INFO: 10
  - WARNING: 2
  - ERROR: 3
- **File**: Same summary saved to a file (e.g. `log_summary.json` or `summary.txt`).

## What are the main steps?

1. Read the log file (handle missing file or permission errors).
2. Go through each line and detect INFO / WARNING / ERROR.
3. Keep counts for each level.
4. Print the summary to the terminal.
5. Write the summary to the output file.
