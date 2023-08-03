import json

courses = '{"name": "Arman Ansari", "languages": ["Python", "Java"]}'
print(type(courses))   # <class 'str'>

## Loads method parse the json string and it returns dictionary object
dict_courses = json.loads(courses)
print(type(dict_courses))   # <class 'dict'>
print(dict_courses)  # {'name': 'Arman Ansari', 'languages': ['Python', 'Java']}
print(dict_courses['name'])  # Arman Ansari

## Get me the first language taught by the trainer
print(dict_courses['languages'][0])  # Python



