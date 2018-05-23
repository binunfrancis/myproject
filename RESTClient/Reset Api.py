import requests
import json

CountryCode='US'
API_URL='http://api.bitbucket.org/2.0/repositories/binunfrancis'

Result = requests.get(API_URL,headers={'content-type': 'application/json'},verify=False)
if Result.status_code==200:
    #print (Result.text)
    ResultJSON=json.loads(Result.text)
    s=0
    while s<3:
        print(ResultJSON['values'][s]['name'])
        print(ResultJSON['values'][s]['links']['clone'][-1]['href'])
        s=s+1
    #print(ResultJSON['values'][0]['links']['clone'][-1] ['href'])
    #print(ResultJSON['values'][1]['links']['clone'][-1])
   # print(ResultJSON['values'][2]['links']['clone'][-1])
   