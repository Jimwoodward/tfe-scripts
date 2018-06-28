from teams import call_teams

response_payload = call_teams()

for team in response_payload['data']:
    print('Team name: {}'.format(team['attributes']['name'])+' ::::: '+'Team id: {}'.format(team['id']))
