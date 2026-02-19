import json
import os


def read_log_file(path):
    try:
        with open(path, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except PermissionError:
        print(f"Permission denied: {path}")
        return None


def analyze_logs(lines):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if " INFO " in line:
            counts["INFO"] += 1
        elif " WARNING " in line:
            counts["WARNING"] += 1
        elif " ERROR " in line:
            counts["ERROR"] += 1
    return counts


def print_summary(counts):
    print("Log Analysis Summary")
    print("-" * 24)
    for level, count in counts.items():
        print(f"  {level}: {count}")
    print("-" * 24)


def write_summary(counts, output_path):
    with open(output_path, "w") as f:
        json.dump(counts, f, indent=2)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, "..", "app.log")
    output_path = os.path.join(script_dir, "log_summary.json")
    lines = read_log_file(log_path)
    if lines is None:
        return
    if not lines:
        print("Log file is empty.")
        return
    counts = analyze_logs(lines)
    print_summary(counts)
    write_summary(counts, output_path)
    print(f"Summary written to {output_path}")


if __name__ == "__main__":
    main()
