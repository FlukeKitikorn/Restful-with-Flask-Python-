import requests

URL = 'https://jsonplaceholder.typicode.com/users'
API_ENDPOINT = 'https://jsonplaceholder.typicode.com/posts'

# target = "thailand"

# PARAMS = {'city':target}

# req = requests.get(url=URL, params=PARAMS)
# req = requests.get(url=URL)
# data = req.json()

# filtered_users = [user for user in data if user['address']['city'].lower() == 'lebsackbury']

# print(filtered_users)

data = {'name': 'Satee'}
headers = {'Content-type': 'application/json; charset=UTF-8'}

req = requests.post(url=API_ENDPOINT, json=data, headers=headers)

print(req.json())