# Positional arguments

# You can also have arguments without --, which are required:

# parser.add_argument("log_file", type=str, help="Path to the log file")

# Usage:

# python log_analyzer.py app.log --level WARNING

args.log_file # "app.log"

No --, must be provided

Great for required inputs


---

# 📝 Python: `stdout`, `stderr`, and Error Printing

### 1️⃣ Standard Streams in Python

| Stream   | Symbol | Purpose                             |
| -------- | ------ | ----------------------------------- |
| `stdin`  | 0      | Input from user / terminal          |
| `stdout` | 1      | Normal output (results, info, logs) |
| `stderr` | 2      | Error messages, warnings            |

* By default, `print()` writes to **`stdout`**.
* Use `print(..., file=sys.stderr)` to write to **`stderr`**.

---

### 2️⃣ Why Use `stderr`?

* Separates **errors** from normal output
* Useful in **scripts, automation, CI/CD pipelines**
* Errors remain visible even if normal output is redirected

**Example:**

```python
import sys

print("Summary: 10 errors found")          # stdout
print("Error: Log file not found!", file=sys.stderr)  # stderr
```

---

### 3️⃣ Redirection in Terminal

**Redirect stdout only:**

```bash
python script.py > output.txt
```

* Normal output → `output.txt`
* Errors → displayed on terminal

**Redirect stderr separately:**

```bash
python script.py > output.txt 2> errors.txt
```

* Normal output → `output.txt`
* Errors → `errors.txt`

**Redirect both together:**

```bash
python script.py > all_output.txt 2>&1
```

* Both stdout and stderr → `all_output.txt`

---

### 4️⃣ Professional Practice

* **Normal results → stdout**
* **Errors, warnings → stderr**
* Makes scripts **automation-friendly** and **debugging easier**

---

### 5️⃣ In OOP / LogAnalyzer Example

```python
import sys

def read_logs(self):
    try:
        with open(self.log_path, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found: {self.log_path}", file=sys.stderr)
        return None
    except PermissionError:
        print(f"Error: Permission denied: {self.log_path}", file=sys.stderr)
        return None
```

* Errors printed to **stderr**
* Normal summary (counts) printed via `print()` → **stdout**

---

💡 **Tip:** Always separate **output** and **errors** in professional scripts — it’s cleaner and compatible with automation tools.

