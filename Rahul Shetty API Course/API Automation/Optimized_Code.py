import requests
from payLoad import addBookPayLoad


addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php', 
                             json=addBookPayLoad('Shukla'),
                             headers={'Content-Type': 'application/json'})



response_json = addBook_response.json()


##############           ----- DELETE Book -----                 ##############

## Extract 'ID' of that book
book_id = response_json['ID']


delBook_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', 
                             json={"ID": book_id}, headers={'Content-Type': 'application/json'})

## Assertions 
assert delBook_response.status_code == 200

res_json = delBook_response.json()
print(res_json['msg'])

## Assertions 
assert res_json['msg'] == "book is successfully deleted" 


