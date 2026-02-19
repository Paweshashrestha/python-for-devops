import json
import os


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
            print(f"File not found: {self.log_path}")
            return None
        except PermissionError:
            print(f"Permission denied: {self.log_path}")
            return None

    def analyze(self, lines):
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
        return self.counts

    def print_summary(self):
        print("Log Analysis Summary")
        print("-" * 24)
        for level, count in self.counts.items():
            print(f"  {level}: {count}")
        print("-" * 24)

    def write_summary(self):
        with open(self.output_path, "w") as f:
            json.dump(self.counts, f, indent=2)
        print(f"Summary written to {self.output_path}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, "..", "app.log")
    output_path = os.path.join(script_dir, "log_summary.json")
    analyzer = LogAnalyzer(log_path, output_path)
    lines = analyzer.read_logs()
    if lines is None:
        return
    if not lines:
        print("No logs to analyze.")
        return
    analyzer.analyze(lines)
    analyzer.print_summary()
    analyzer.write_summary()


if __name__ == "__main__":
    main()
