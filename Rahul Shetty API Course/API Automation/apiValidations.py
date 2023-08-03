import requests
import json

response = requests.get('http://216.10.245.166//Library/GetBook.php', 
                        params={'AuthorName': 'joshua little'})

print(response)   # <Response [200]>
print(response.text)   # [{"book_name":"Raj","isbn":"bcdf","aisle":"2290"}]
print(response.content)  # b'[{"book_name":"Raj","isbn":"bcdf","aisle":"2290"}]'
print(type(response.text))  # <class 'str'>
print(type(response.content))  # <class 'bytes'>


r"""Parse json string to 'dict'.

:Output is of 'list' type hence, it is giving 'list' as the type instead of 'dict'
"""
data = json.loads(response.text)   
print(data)  # [{'book_name': 'Raj', 'isbn': 'bcdf', 'aisle': '2290'}]
print(type(data))  # <class 'list'>

# get the 1st 'isbn'
print(data[0]['isbn'])  # bcdf