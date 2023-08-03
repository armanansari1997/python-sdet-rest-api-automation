import json

#######  Compare two(2) json Schemas using python dictionaries with example   ########

## here we can use single forward slash(/) or double backward slash(\\)
with open('Rahul Shetty API Course\\JsonFileParsing\dummy_course.json') as file1:
    data1 = json.load(file1)
    
with open('Rahul Shetty API Course\\JsonFileParsing\\dummy_course2.json') as file2:
    data2 = json.load(file2)

    ## comparing two dict object
    print(data1 == data2)
    
    
    ## Extra Steps
    ## using Assertion concept
    assert data1 == data2  # AssertionError
        
        




