from fastapi import FastAPI
from pathlib import Path

app = FastAPI(title="DevOps API")

LOG_FILE = Path(__file__).resolve().parent / "app.log"


@app.get("/health")
def health():
    return {"status": "ok"}


def analyze_logs(path):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if " INFO " in line:
                    counts["INFO"] += 1
                elif " WARNING " in line:
                    counts["WARNING"] += 1
                elif " ERROR " in line:
                    counts["ERROR"] += 1
    except FileNotFoundError:
        return None
    return counts


@app.get("/logs")
def logs():
    if not LOG_FILE.exists():
        return {"error": "Log file not found", "path": str(LOG_FILE)}
    summary = analyze_logs(LOG_FILE)
    return {"summary": summary}


@app.get("/aws")
def aws():
    try:
        import boto3

        ec2 = boto3.client("ec2")
        s3 = boto3.client("s3")
        instances = []
        for r in ec2.describe_instances().get("Reservations", []):
            for i in r.get("Instances", []):
                instances.append(
                    {"instance_id": i["InstanceId"], "state": i["State"]["Name"]}
                )
        buckets = [b["Name"] for b in s3.list_buckets().get("Buckets", [])]
        return {"ec2_instances": instances, "s3_buckets": buckets}
    except Exception as e:
        return {"error": str(e)}
