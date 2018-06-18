import requests
import os

token = 'Bearer '+os.environ['TOKEN']
headers = {'Authorization': token}

parameters = {'page[size]': '100', 'page[number]': '1'}
response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=parameters)
file = open("workspaces.txt", "w")
total_pages=response.json()['meta']['pagination']['total-pages']


for pages in range(1, total_pages+1):
    parameters = {'page[size]': '100', 'page[number]': pages}
    response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=parameters)

    for workspace in response.json()['data']:
        file.write(workspace['attributes']['name']+'\n')

file.close()
