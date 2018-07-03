import requests
import time
import os

def call_team_workspaces_get(workspace_id):
    token = 'Bearer '+os.environ['TOKEN']
    headers = {'Authorization': token}
    team_workspaces_parameters = {'filter[workspace][id]': '{}'.format(workspace_id)}
    team_workspaces_response = requests.get('https://app.terraform.io/api/v2/team-workspaces', headers=headers, params=team_workspaces_parameters)
    response_payload = team_workspaces_response.json()
    return response_payload

def call_team_workspaces_post(access_level, workspace_id, team_id):
    token = 'Bearer '+os.environ['TOKEN']
    headers = {'Authorization': token, 'Content-Type': 'application/vnd.api+json'}
    payload = {'data':{'attributes':{'access':access_level},'relationships':{'workspace':{'data':{'type':'workspaces','id':workspace_id}},'team':{'data':{'type':'teams','id':team_id}}},'type':'team-workspaces'}}
    team_workspaces_response = requests.post('https://app.terraform.io/api/v2/team-workspaces', headers=headers, json=payload)
    print(team_workspaces_response.raise_for_status)

def list_workspace_access_verbose(workspaces_list, workspace_id):
    response_payload = call_team_workspaces(workspace_id)

    for workspace in workspaces_list:
        if workspace['id'] == workspace_id:
            yield '{} : Workspace name ::::: {} : Workspace id'.format(workspace['attributes']['name'], workspace_id)
    for teams in response_payload['data']:
        yield '{} : Team name ::::: {} : Team id'.format(teams['relationships']['team']['links']['related'].split('/')[4], teams['relationships']['team']['data']['id'])

def list_workspace_access(workspace_id):
    response_payload = call_team_workspaces(workspace_id)

    for teams in response_payload['data']:
        yield teams['relationships']['team']['data']['id']
