import json

#######  Parsing compex json with nested Structure and extract values   ######

## here we can use single forward slash(/) or double backward slash(\\)
with open('Rahul Shetty API Course\\JsonFileParsing\\dummy_course.json') as file:
    data = json.load(file)
    print(data)
    print(type(data))

## get the price of 'RPA' using indexing
print(data['courses'][2]['price'])


## important
## get the price of 'RPA' w/o using indexing because index is dynamic
for course in data['courses']:
    if course['title'] == 'RPA':
        print(course['price'])
        
        # For jsonParsing use till above steps
        # Extra steps
        # Some assertions using here for practice
        try:
            assert course['price'] < 45, "price is not less than 45"
        except AssertionError as e:
            # Handling Assertion error
            print("Assertion failed")
        # This will print 'Hello' because exception is caught in except block
        print("Hello")




