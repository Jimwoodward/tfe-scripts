import sys, json
from team_workspaces import call_team_workspaces_post

payload_path = sys.argv[1]
team_id = sys.argv[2]
with open(payload_path, 'r') as payload_file:
    team_workspaces_access_list = json.load(payload_file)

for workspace in team_workspaces_access_list['data']:
    status_code = call_team_workspaces_post(workspace['access_level'], workspace['workspace_id'], team_id)
    if status_code == 201:
        print('Team {} has been added to {} ({}) and given {} access'.format(team_id, workspace['workspace_name'], workspace['workspace_id'], workspace['access_level']))
    elif status_code == 422:
        print('Error. Team ({}) was not able to be added to {} ({}) with {} access. POST failed with HTTP error code: {}. The team may already have access to this workspace'.format(team_id, workspace['workspace_name'], workspace['workspace_id'], workspace['access_level'], status_code))
    else:
        print('Error. Team ({}) was not able to be added to {} ({}) with {} access. POST failed with HTTP error code: {}'.format(team_id, workspace['workspace_name'], workspace['workspace_id'], workspace['access_level'], status_code))