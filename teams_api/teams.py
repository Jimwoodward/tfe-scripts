import requests, os

def call_teams():
    token = 'Bearer '+os.environ['TOKEN']
    headers = {'Authorization': token}
    teams_response = requests.get('https://app.terraform.io/api/v2/organizations/snag/teams', headers=headers)
    response_payload = teams_response.json()
    return response_payload

def list_team_names():
    response_payload = call_teams()

    for team in response_payload['data']:
        yield team['attributes']['name']

def list_team_members(team_id):
    response_payload = call_teams()

    for team in response_payload['data']:
        if team_id == team['id']:
            print(team_id)
            for users in team['relationships']['users']['data']:
                yield users['id']

