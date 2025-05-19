import requests
import os

API_KEY = os.environ.get("ABUSEIPDB_API_KEY")
OUTPUT_FILE = "blocklist.txt"
CONFIDENCE_MIN = 90
LIMIT = 10000

url = "https://api.abuseipdb.com/api/v2/blacklist"
headers = {
    "Key": API_KEY,
    "Accept": "text/plain"
}
params = {
    "confidenceMinimum": CONFIDENCE_MIN,
    "limit": LIMIT
}

print(f"[*] Fetching AbuseIPDB IPs with confidence >= {CONFIDENCE_MIN}")
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    with open(OUTPUT_FILE, "w") as f:
        f.write(response.text)
    print(f"[+] Blocklist saved to {OUTPUT_FILE}")
else:
    print(f"[!] Failed to fetch data: {response.status_code}")
    print(response.text)
