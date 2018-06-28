import requests
import json
import os
import sys

token = 'Bearer '+os.environ["TOKEN"]
headers = {'Authorization': token, 'Content-Type': 'application/vnd.api+json'}

response = requests.delete('https://app.terraform.io/api/v2/team-workspaces/{}'.format('tws-2NQkiw4u78iwdhfq'), headers=headers)
