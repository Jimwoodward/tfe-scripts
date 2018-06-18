import requests
import os

token = 'Bearer '+os.environ["TOKEN"]
headers = {'Authorization': token}
response = requests.get('https://app.terraform.io/api/v2/organizations/snag/teams', headers=headers)

for team in response.json()["data"]:
    print ("Team name: {}".format(team["attributes"]["name"])+" ::::: "+"Team id: {}".format(team["id"]))
