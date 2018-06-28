from workspaces_api.workspaces import create_workspace_ids_list, list_workspace_id
from team_workspaces import list_workspace_access_verbose

workspaces_list = create_workspace_ids_list()

for workspace_id in list_workspace_id(workspaces_list):
    for results in list_workspace_access_verbose(workspaces_list, workspace_id):
        print(results)
