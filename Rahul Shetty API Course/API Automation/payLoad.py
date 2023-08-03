def addBookPayLoad(isbn):
    body = {
                "name": "Learn API with Meta",
                "isbn": isbn,
                "aisle": "743920",
                "author": "Meta little"
            }
    return body