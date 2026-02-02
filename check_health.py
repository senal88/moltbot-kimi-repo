import requests
import os
from dotenv import load_dotenv

load_dotenv()
url = f"{os.getenv('CLAWDBOT_GW_URL')}/api/health"
headers = {"Authorization": f"Bearer {os.getenv('CLAWDBOT_GW_TOKEN')}"}

try:
    response = requests.get(url, headers=headers, timeout=5)
    status = "ONLINE" if response.status_code in [200, 404] else "ISSUES"
    print(f"Status: {status} ({response.status_code})")
except Exception as e:
    print(f"Status: OFFLINE - {e}")
