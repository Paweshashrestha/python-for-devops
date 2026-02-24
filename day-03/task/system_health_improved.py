import psutil
     
def get_thresholds(default=(80, 80, 80)):
    try:
        values = tuple(
            int(input(f"Enter {name} threshold (%): "))
            for name in ("CPU", "Memory", "Disk")
        )

        if any(not 0 <= x <= 100 for x in values):
            raise ValueError("Thresholds must be between 0 and 100")

        return values

    except ValueError as e:
        print(f"Invalid input: {e}. Using defaults {default}.")
        return default

def get_metrics():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        return {
            "cpu": cpu_percent,
            "memory": memory.percent,
            "disk": disk.percent,
        }
    except Exception as e:
        print(f"Failed to read metrics: {e}")
        return None


def check_metrics(metrics, thresholds):
    cpu_t, mem_t, disk_t = thresholds
    results = []
    if metrics["cpu"] > cpu_t:
        results.append(f"CPU alert: {metrics['cpu']}% > {cpu_t}%")
    else:
        results.append(f"CPU OK: {metrics['cpu']}%")
    if metrics["memory"] > mem_t:
        results.append(f"Memory alert: {metrics['memory']}% > {mem_t}%")
    else:
        results.append(f"Memory OK: {metrics['memory']}%")
    if metrics["disk"] > disk_t:
        results.append(f"Disk alert: {metrics['disk']}% > {disk_t}%")
    else:
        results.append(f"Disk OK: {metrics['disk']}%")
    return results


def main():
    thresholds = get_thresholds()
    metrics = get_metrics()
    if metrics is None:
        return
    for line in check_metrics(metrics, thresholds):
        print(line)


if __name__ == "__main__":
    main()
