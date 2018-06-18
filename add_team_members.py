import requests
import os
import sys
import json

team_id = str(sys.argv[1])
payload = sys.argv[2]

print (team_id)
print (payload)

token = 'Bearer '+os.environ["TOKEN"]
headers = {'Authorization': token}

response = requests.post('https://app.terraform.io/api/v2/teams/{}/relationships/users'.format(team_id), headers=headers, data=payload)

print (response.url)
print (response.json())
