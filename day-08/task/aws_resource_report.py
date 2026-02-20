import json
import os
import boto3


def list_ec2_instances():
    ec2 = boto3.client("ec2")
    result = ec2.describe_instances()
    instances = []
    for reservation in result.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            instances.append({
                "instance_id": instance["InstanceId"],
                "state": instance["State"]["Name"],
            })
    return instances


def list_s3_buckets():
    s3 = boto3.client("s3")
    result = s3.list_buckets()
    return [b["Name"] for b in result.get("Buckets", [])]


def main():
    try:
        ec2_list = list_ec2_instances()
        bucket_list = list_s3_buckets()
    except Exception as e:
        print(f"Error connecting to AWS: {e}")
        return
    report = {
        "ec2_instances": ec2_list,
        "s3_buckets": bucket_list,
    }
    print("EC2 instances (id, state):")
    for i in ec2_list:
        print(f"  {i['instance_id']}  {i['state']}")
    print("\nS3 buckets:")
    for b in bucket_list:
        print(f"  {b}")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, "aws_report.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved to {out_path}")


if __name__ == "__main__":
    main()
