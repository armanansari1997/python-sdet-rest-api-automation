import requests

response = requests.get('http://216.10.245.166//Library/GetBook.php', 
                        params={'AuthorName': 'joshua little'})


# Better than previous module (apiValidations.py) code 
json_response = response.json()
print(json_response)
print(type(json_response))  # <class 'list'>

# get the 2nd 'isbn'
print(json_response[1]['isbn'])  # bcdf