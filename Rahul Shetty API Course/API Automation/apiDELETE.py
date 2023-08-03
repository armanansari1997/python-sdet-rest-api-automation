import requests

json_data = {
            "name": "Learn API with Meta",
            "isbn": "Meta",
            "aisle": "76378274400",
            "author": "Meta little"
            }


addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php', 
                             json=json_data,
                             headers={'Content-Type': 'application/json'})



response_json = addBook_response.json()
print(addBook_response.status_code)

## Extract 'ID' of that book
book_id = response_json['ID']

##############           ----- DELETE Book -----                 ##############


delBook_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', 
                             json={"ID": book_id}, headers={'Content-Type': 'application/json'})
print(book_id)

## Assertions 
# assert delBook_response.status_code == 200

res_json = delBook_response.json()
print(res_json['msg'])

## Assertions 
assert res_json['msg'] == "book is successfully deleted" 


