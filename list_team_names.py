import requests
import os

token = 'Bearer '+os.environ['TOKEN']
headers = {'Authorization': token}
response = requests.get('https://app.terraform.io/api/v2/organizations/snag/teams', headers=headers)

#print (len(response.json()["data"]))
#num_of_teams = len(response.json()["data"])

for team in response.json()["data"]:
    print ('Team name: {}'.format(team["attributes"]["name"]))
#print ('Response: {0}'.format(response.json()['data']))
