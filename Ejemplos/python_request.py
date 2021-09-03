import requests
import json

url = 'https://reqres.in/api/users?page=1'

response = requests.get(url)

print(type(response), response)
print(response.status_code)
print(response.text)
print(response.json())
print(json.dumps(response.json(), indent=4))

