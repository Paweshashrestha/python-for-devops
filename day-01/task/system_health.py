import psutil


def get_thresholds():
    cpu = int(input("Enter CPU threshold (%): "))
    memory = int(input("Enter memory threshold (%): "))
    disk = int(input("Enter disk threshold (%): "))
    return cpu, memory, disk


def get_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    return {
        "cpu": cpu_percent,
        "memory": memory.percent,
        "disk": disk.percent,
    }


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
    for line in check_metrics(metrics, thresholds):
        print(line)


if __name__ == "__main__":
    main()
