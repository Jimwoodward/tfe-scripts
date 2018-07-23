from teams_api.teams import call_teams

def team_workspace_access_generator(team_id, access_level):
    response_payload = call_teams()
    for team in response_payload['data']:
      if team_id == team['id']:
        team_name = team['attributes']['name']
    
    team = {team_name:team_id}

    print(team)