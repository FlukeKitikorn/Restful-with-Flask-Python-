import requests

URL = 'https://jsonplaceholder.typicode.com/users'
API_ENDPOINT = 'https://jsonplaceholder.typicode.com/posts'
API_ENDPOINT_PUT = 'https://jsonplaceholder.typicode.com/posts/1'
API_ENDPOINT_PATCH = 'https://jsonplaceholder.typicode.com/posts/1'
# API_ENDPOINT_DELETE = 

# target = "thailand"

# PARAMS = {'city':target}

# req = requests.get(url=URL, params=PARAMS)
# req = requests.get(url=URL)
# data = req.json()

# filtered_users = [user for user in data if user['address']['city'].lower() == 'lebsackbury']

# print(filtered_users)

# data = {'name': 'Satee'}
# headers = {'Content-type': 'application/json; charset=UTF-8'}

# req = requests.post(url=API_ENDPOINT, json=data, headers=headers)

# response 201 = success
# check more HTTP code status in this link : https://restfulapi.net/http-status-codes/
# print(req.json())


'''
payload = { 'id': 1, 
           'title': 'foo',
           'body': 'bar',
           'userId': 1
          }
headers = {'Content-type': 'application/json; charset=UTF-8'}

res = requests.put(url=API_ENDPOINT_PUT, json=payload, headers=headers)
print(res.json())'''

'''
data = {'title': 'foo'}
headers = {'Content-type': 'application/json; charset=UTF-8'}

res = requests.patch(url=API_ENDPOINT_PATCH, json=data, headers=headers)
print(res)
print(res.json())'''

res = requests.delete(url=API_ENDPOINT_PATCH)
print(res)
print(res.json())