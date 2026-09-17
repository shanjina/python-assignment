import requests

url = "https://www.google.com"

response = requests.get(url)

print("HTTP Status Code:", response.status_code)