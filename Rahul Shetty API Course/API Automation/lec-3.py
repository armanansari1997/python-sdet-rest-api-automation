import requests

response = requests.get('http://216.10.245.166//Library/GetBook.php', 
                        params={'AuthorName': 'joshua little'})

json_response = response.json()

# get the status code of reponse
print(response.status_code)  # 200

# Assertions
assert response.status_code == 200

# get all the headers of the response
print(response.headers)

# get the content-type header only
print(response.headers['content-type'])  # application/json;charset=UTF-8

# Assertions
assert response.headers['content-type'] == 'application/json;charset=UTF-8'
 