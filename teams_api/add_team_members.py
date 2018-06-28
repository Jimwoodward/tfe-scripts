import requests
import os
import sys
import json

team_id = str(sys.argv[1])
payload_path = sys.argv[2]

with open(payload_path, 'r') as payload_file:
    payload = json.load(payload_file)

token = 'Bearer '+os.environ["TOKEN"]
headers = {'Authorization': token, 'Content-Type': 'application/vnd.api+json'}

response = requests.post('https://app.terraform.io/api/v2/teams/{}/relationships/users'.format(team_id), headers=headers, json=payload)
