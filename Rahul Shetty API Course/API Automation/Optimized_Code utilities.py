import requests
from payLoad import addBookPayLoad
from utilities.configurations import *
from utilities.resources import *


# config = get_config()
url = get_config()['API']['endpoint'] + APIResources.add_book
headers = {'Content-Type': 'application/json'}

addBook_response = requests.post(url, json=addBookPayLoad('Shukla'), headers=headers)



response_json = addBook_response.json()


##############           ----- DELETE Book -----                 ##############

## Extract 'ID' of that book
book_id = response_json['ID']

url = get_config()['API']['endpoint'] + APIResources.delete_book
headers = {'Content-Type': 'application/json'}

delBook_response = requests.post(url , json={"ID": book_id}, headers=headers)

## Assertions 
assert delBook_response.status_code == 200

res_json = delBook_response.json()
print(res_json['msg'])

## Assertions 
assert res_json['msg'] == "book is successfully deleted" 


