import requests
from utilities.configurations import *
from utilities.resources import *

# Changed
url = get_config()['API']['endpoint'] + APIResources.get_book
response = requests.get(url, params={'AuthorName': 'joshua little'})


# Better than previous module (apiValidations.py) code 
json_response = response.json()
print(json_response)
print(type(json_response))  # <class 'list'>

# get the 1st 'isbn'
print(json_response[0]['isbn'])  # bcdf