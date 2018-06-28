import requests
import os
import json

def call_teams_post(payload, team_id):
    token = 'Bearer '+os.environ['TOKEN']
    headers = {'Authorization': token, 'Content-Type': 'application/vnd.api+json'}
    teams_response = requests.post('https://app.terraform.io/api/v2/teams/{}/relationships/users'.format(team_id), headers = headers, json = payload)
    return teams_response

def add_team_member(user_name, team_id):
    payload = {'data':[{'type':'users','id':user_name}]}
    response_payload = call_teams_post(payload, team_id)
    yield response_payload