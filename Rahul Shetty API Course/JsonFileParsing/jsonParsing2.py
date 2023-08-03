import json

#######        Parse content present in json file into dictionary          ######

## here we can use single forward slash(/) or double backward slash(\\)
with open('Rahul Shetty API Course\\JsonFileParsing\\dummy_course.json') as file:
    data = json.load(file)
    print(data)
    print(type(data))  # <class 'dict'>

## Print 2nd courses title
print(data['courses'][1]['title'])

## Print website name
print(data['dashboard']['website'])



