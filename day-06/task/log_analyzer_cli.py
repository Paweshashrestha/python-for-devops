import json
import sys
import argparse


class LogAnalyzer:
    def __init__(self, log_path, output_path="log_summary.json"):
        self.log_path = log_path
        self.output_path = output_path
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    def read_logs(self):
        try:
            with open(self.log_path, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            print(f"File not found: {self.log_path}", file=sys.stderr)
            return None
        except PermissionError:
            print(f"Permission denied: {self.log_path}", file=sys.stderr)
            return None

    def analyze(self, lines, level_filter=None):
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if " INFO " in line:
                self.counts["INFO"] += 1
            elif " WARNING " in line:
                self.counts["WARNING"] += 1
            elif " ERROR " in line:
                self.counts["ERROR"] += 1
        if level_filter:
            # Dictionary Comprehension
            self.counts = {k: v for k, v in self.counts.items() if k == level_filter}
            # print(type(self.counts))
        return self.counts

    def print_summary(self, level_filter=None):
        data = (
            self.counts
            if not level_filter
            else {level_filter: self.counts.get(level_filter, 0)}
        )
        print("Log Analysis Summary")
        print("-" * 24)
        for level, count in data.items():
            print(f"  {level_filter}: {count}")
        print("-" * 24)

    def write_summary(self, level_filter=None):
        data = (
            self.counts
            if not level_filter
            else {level_filter: self.counts.get(level_filter, 0)}
        )
        with open(self.output_path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Summary written to {self.output_path}")


def main():
    # Create a parser
    parser = argparse.ArgumentParser(description="Analyze logs")
    # Define the arguments the script accepts
    parser.add_argument(
        "--level_filter",
        type=str,
        choices=["INFO", "WARNING", "ERROR"],
        help="Filter log by level_filter",
    )
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--out", default="summary.json", help="Output file path")
    # Parse the arguments from the command line
    args = parser.parse_args()
    print("Argument input ", args.level_filter)

    analyzer = LogAnalyzer(args.file, args.out)
    lines = analyzer.read_logs()
    if lines is None:
        sys.exit(1)
    if not lines:
        print("No logs to analyze.")
        return
    analyzer.analyze(lines, args.level)
    analyzer.print_summary(args.level)
    analyzer.write_summary(args.level)


if __name__ == "__main__":
    main()
