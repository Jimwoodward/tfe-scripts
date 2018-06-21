import requests

def list_workspace_access(token, workspace_id):
    headers = {'Authorization': token}

    team_workspaces_parameters = {'filter[workspace][id]': '{}'.format(workspace_id)}
    team_workspaces_response = requests.get('https://app.terraform.io/api/v2/team-workspaces', headers=headers, params=team_workspaces_parameters)

    workspace_name_parameters = {'page[size]': '100', 'page[number]': '1'}
    workspace_name_response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=workspace_name_parameters)

    total_pages=workspace_name_response.json()['meta']['pagination']['total-pages']

    print (total_pages)
    for pages in range(1, total_pages+1):
        parameters = {'page[size]': '100', 'page[number]': pages}
        response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=parameters)

        for workspace in response.json()['data']:
            if workspace['id'] == workspace_id:
                print ('Workspace name: {}'.format(workspace['attributes']['name']))

    print ('Workspace id: {}'.format(workspace_id))
    for teams in team_workspaces_response.json()['data']:
        print (teams['relationships']['team']['data']['id']+' ::::: '+teams['relationships']['team']['links']['related'].split('/')[4])


def list_workspace_ids(token, human_readable):
    headers = {'Authorization': token}

    parameters = {'page[size]': '100', 'page[number]': '1'}
    response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=parameters)
    total_pages=response.json()['meta']['pagination']['total-pages']

    if human_readable == 'True':

        file = open('workspace_ids.txt', 'w')

        for pages in range(1, total_pages+1):
            parameters = {'page[size]': '100', 'page[number]':pages}
            response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=parameters)

            for workspace in response.json()['data']:
                file.write('Team name: {} ::::: '.format(workspace['attributes']['name']))
                file.write('Workspace id: {}'.format(workspace['id']+'\n'))
    elif human_readable == 'False':
        for pages in range(1, total_pages+1):
            parameters = {'page[size]': '100', 'page[number]':pages}
            response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=parameters)

            for workspace in response.json()['data']:
                return workspace["id"]
    else:
        print('"Human Readable" flag set incorrectly. The value should be "True" or "False". The value was: {}'.format(human_readable))
