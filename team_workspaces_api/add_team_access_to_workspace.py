import os
import requests
import json
import sys

payload_path = sys.argv[1]

with open(payload_path, 'r') as payload_file:
    payload = json.load(payload_file)

token = 'Bearer '+os.environ["TOKEN"]
headers = {'Authorization': token, 'Content-Type': 'application/vnd.api+json'}

response = requests.post('https://app.terraform.io/api/v2/team-workspaces')
