import requests

url = "https://www.ecfr.gov/api/version/latest/collections"
response = requests.get(url)
print(response.status_code)
print(response.text[:300])  # print first 300 chars to check content

