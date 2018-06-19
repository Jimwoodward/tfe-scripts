import requests
import os
import sys

team_id = str(sys.argv[1])

token = 'Bearer '+os.environ['TOKEN']
headers = {'Authorization': token}
response = requests.get('https://app.terraform.io/api/v2/organizations/snag/teams', headers=headers)

for team in response.json()["data"]:
    if team_id == team["id"]:
        for users in team["relationships"]["users"]["data"]:
            print (users["id"])
