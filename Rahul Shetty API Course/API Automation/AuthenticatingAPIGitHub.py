import requests

from getpass import getpass, getuser

# ============================= Authentication ========================#

url = 'https://api.github.com/user'
user = getpass(f"Enter Username : {getuser()}")
password = getpass('Enter your Password : ')

r'''not Working  ### getting 401 status code
'''
github_response = requests.get(url, auth=(user, password))

r'''
 github_response = requests.get(url, verify=False, auth=(user, password))
 print(user)
 print(password)
'''

print('Status Code :', github_response.status_code)





