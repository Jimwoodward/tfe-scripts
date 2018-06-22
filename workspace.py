import requests

def list_workspace_ids(token, human_readable):
    headers = {'Authorization': token}
    parameters = {'page[size]': '100', 'page[number]': '1'}
    response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=parameters)
    total_pages=response.json()['meta']['pagination']['total-pages']

    if human_readable == 'True':
        for pages in range(1, total_pages+1):
            parameters = {'page[size]': '100', 'page[number]':pages}
            response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=parameters)

            for workspace in response.json()['data']:
                yield 'Team name: {} ::::: Workspace id: {}'.format(workspace['attributes']['name'], workspace['id'])
    elif human_readable == 'False':
        for pages in range(1, total_pages+1):
            parameters = {'page[size]': '100', 'page[number]':pages}
            response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=parameters)

            for workspace in response.json()['data']:
                yield workspace["id"]

def list_workspace_access(token, workspace_id):
    headers = {'Authorization': token}
    team_workspaces_parameters = {'filter[workspace][id]': '{}'.format(workspace_id)}
    team_workspaces_response = requests.get('https://app.terraform.io/api/v2/team-workspaces', headers=headers, params=team_workspaces_parameters)
    response_payload = team_workspaces_response.json()

    for teams in response_payload['data']:
        yield teams['relationships']['team']['data']['id']
        #print(teams['relationships']['team']['data']['id']+' ::::: '+teams['relationships']['team']['links']['related'].split('/')[4])
        #workspace_payload = requests.get('https://app.terraform.io/{}'.format(teams['relationships']['workspace']['links']['related']))
        #print(workspace_payload.url)
        #print(workspace_payload)

        workspace_name_parameters = {'page[size]': '100', 'page[number]': '1'}
        workspace_name_response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=workspace_name_parameters)

        total_pages=workspace_name_response.json()['meta']['pagination']['total-pages']

        # grab_next = True
        # page = 1
        #
        # while grab_next:
        #     workspace_name_parameters = {'page[size]': '100', 'page[number]': page}
        #     workspace_name_response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=workspace_name_parameters)
        #     response_payload = workspace_name_response.json()
        #
        #     for workspace in response_payload['data']:
        #         if workspace['id'] == workspace_id:
        #             print ('Workspace name: {}'.format(workspace['attributes']['name']))
        #
        #     print ('Workspace id: {}'.format(workspace_id))
        #     for teams in team_workspaces_response.json()['data']:
        #         print (teams['relationships']['team']['data']['id']+' ::::: '+teams['relationships']['team']['links']['related'].split('/')[4])
        #
        #     page = response_payload['meta']['pagination']['next-page']
        #
        #     if page is None:
        #         grab_next = False
