import requests

url = input("URL: ")

headers = {
    "Range": "bytes=0-99"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(len(response.content))