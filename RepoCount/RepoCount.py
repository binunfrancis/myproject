import requests
import json

API_URL='http://api.bitbucket.org/2.0/repositories/binunfrancis'

Result = requests.get(API_URL,headers={'content-type': 'application/json'},verify=False)
if Result.status_code==200:
 #   print (Result.text)
    ResultJSON=json.loads(Result.text)

for i in range(0,len(ResultJSON)):
     print(ResultJSON['values'][i]['name'])

