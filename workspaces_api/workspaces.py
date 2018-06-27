import requests, os

def call_workspaces(page_number, page_size):
    token = 'Bearer '+os.environ['TOKEN']
    headers = {'Authorization': token}
    workspace_ids_parameters = {'page[size]': page_size, 'page[number]': page_number}
    workspace_ids_response = requests.get('https://app.terraform.io/api/v2/organizations/snag/workspaces', headers=headers, params=workspace_ids_parameters)
    response_payload = workspace_ids_response.json()
    return response_payload

def create_workspace_ids_list():
    grab_next = True
    page = 1
    workspace_list = []

    while grab_next:
        response_payload = call_workspaces(page, 100)
        for workspace in response_payload['data']:
            workspace_list.append(workspace)

        page = response_payload['meta']['pagination']['next-page']

        if page is None:
            grab_next = False

    return workspace_list

def list_workspace_id_verbose(workspaces_list):
    for workspace in workspaces_list:
        yield 'Workspace name: {} ::::: Workspace id: {}'.format(workspace['attributes']['name'], workspace['id'])

def list_workspace_id(workspaces_list):
    for workspace in workspaces_list:
        yield workspace['id']

#def list_workspace_access(token, workspace_id, human_readable, workspaces_list):
    # headers = {'Authorization': token}
    # team_workspaces_parameters = {'filter[workspace][id]': '{}'.format(workspace_id)}
    # team_workspaces_response = requests.get('https://app.terraform.io/api/v2/team-workspaces', headers=headers, params=team_workspaces_parameters)
    # response_payload = team_workspaces_response.json()

    # if human_readable == 'False':
    #     yield workspace_id
    #     for teams in response_payload['data']:
    #         yield teams['relationships']['team']['data']['id']

    # elif human_readable == 'True':
    #     for workspace in workspaces_list:
    #         if workspace['id'] == workspace_id:
    #             yield '{} ::::: Workspace name'.format(workspace['attributes']['name'])
    #
    #     for teams in response_payload['data']:
    #         yield teams['relationships']['team']['links']['related'].split('/')[4]+' ::::: '+teams['relationships']['team']['data']['id']

    # elif human_readable == 'Raw':
    #     yield workspace_id
    #     yield response_payload
