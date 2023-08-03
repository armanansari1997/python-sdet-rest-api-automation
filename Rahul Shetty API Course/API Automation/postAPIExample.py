import requests

json_data = {
            "name": "Learn API with Mark",
            "isbn": "mark",
            "aisle": "2000",
            "author": "Mark little"
            }
addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php', 
                             json=json_data,
                             headers={'Content-Type': 'application/json'})

response_json = addBook_response.json()
print(response_json)
print(type(response_json))  # <class 'dict'>

# for key, val in response_json.items():
#     print(key, val, sep=' : ')

## Extract 'ID' of that book
book_id = response_json['ID']
print(book_id)
