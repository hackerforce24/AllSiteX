
import json

ADMIN_USER = "admin"
ADMIN_PASS = "1213"

def show_logs():
    try:
        with open("logs/db.json", "r") as f:
            for line in f:
                entry = json.loads(line.strip())
                print(f"[{entry['timestamp']}] {entry['user']} downloaded {entry['filename']} from {entry['link']} ({entry['ip']})")
    except FileNotFoundError:
        print("❌ No log file found.")

def login():
    user = input("👤 Admin Username: ")
    pw = input("🔒 Admin Password: ")
    if user == ADMIN_USER and pw == ADMIN_PASS:
        print("✅ Access granted.")
        show_logs()
    else:
        print("❌ Access denied.")

if __name__ == "__main__":
    login()
