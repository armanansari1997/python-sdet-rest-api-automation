import requests

response = requests.get('http://216.10.245.166//Library/GetBook.php', 
                        params={'AuthorName': 'Rahul Shetty'})

json_response = response.json()

#######                  ------- Some Logical Validations -------          ############

# Retrieve the book details with 'ISBN'='MWA697' 
for actualBook in json_response:
    if actualBook['isbn'] == 'MWA697':
        print(actualBook)
        break

expectedBook = {'book_name': 'Jungle Book Deepthi', 'isbn': 'MWA697', 'aisle': '339'}

## Assertions
assert actualBook  == expectedBook

r"""
Note:
    If we don't use 'break' keyword in for loop then we will get the AssertionError
    at the time of comparision. Because, loop will be iterate till last and we are comparing with expectedBook and the last actualBook 
    Hence value are not equal, (AssertionError)
"""
