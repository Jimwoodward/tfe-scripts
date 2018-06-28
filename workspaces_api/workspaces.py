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