import os
import requests
import base64
import schedule
import time
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")
FILE_NAME = os.getenv("FILE_NAME", "README.md")

# API URL GitHub
API_URL = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_NAME}"

def auto_commit():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running auto commit now..")

    res = requests.get(API_URL, headers={
        "Authorization": f"token {ACCESS_TOKEN}"
    })
    
    if res.status_code != 200:
        print("Couldn't get a files:", res.json())
        return
    
    data = res.json()
    sha = data["sha"]


    content = base64.b64decode(data["content"]).decode()

    new_line = f"\nUpdate at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    updated_content = content + new_line


    payload = {
        "message": f"auto update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "content": base64.b64encode(updated_content.encode()).decode(),
        "sha": sha
    }

    push_res = requests.put(API_URL, headers={
        "Authorization": f"token {ACCESS_TOKEN}"
    }, json=payload)

    if push_res.status_code in [200, 201]:
        print("Commit Succeded")
    else:
        print("Try again!", push_res.json())

# 3 hours repeat
schedule.every(10).hours.do(auto_commit)
print("Auto commit service started! Interval: 10 Hours")
while True:
    schedule.run_pending()
    time.sleep(60)
