import json
import os
import requests


def fetch_todos(limit=5):
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"_limit": limit})
    print(type(response))
    response.raise_for_status()
    return response.json()


def process_todos(data):
    completed = [t for t in data if t.get("completed")]
    by_user = {}
    for t in data:
        uid = t.get("userId")
        by_user[uid] = by_user.get(uid, 0) + 1
    return {
        "total": len(data),
        "completed_count": len(completed),
        "by_user_id": by_user,
        "todos": data,
    }


def main():
    data = fetch_todos(10)
    print(type(data))
    print(data)
    processed = process_todos(data)
    print("Summary:")
    print(f"  Total todos: {processed['total']}")
    print(f"  Completed: {processed['completed_count']}")
    print(f"  By user: {processed['by_user_id']}")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, "output.json")
    with open(out_path, "w") as f:
        json.dump(processed, f, indent=2)
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()
