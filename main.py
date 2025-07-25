
import os
import json
from datetime import datetime

def log_download(user, link, filename, ip="127.0.0.1"):
    log_entry = {
        "user": user,
        "link": link,
        "filename": filename,
        "ip": ip,
        "timestamp": datetime.now().isoformat()
    }
    with open("logs/db.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    print(f"✅ Download logged for {user}: {filename}")

def start_downloader():
    print("🔹 AllSiteX Monitor Pro v4.0 🔹")
    user = input("👤 Enter your username: ")
    link = input("🔗 Enter download link: ")
    filename = input("📁 Enter file name to save as: ")
    log_download(user, link, filename)
    print(f"✅ Simulated download complete: {filename}")

if __name__ == "__main__":
    start_downloader()
