import requests
import json

def download_ecfr():
    url = "https://www.ecfr.gov/api/renderer/v1/content/title/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        with open("ecfr_data.json", "w") as f:
            json.dump(data, f, indent=2)
        print("✅ ecfr_data.json created.")
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    download_ecfr()

