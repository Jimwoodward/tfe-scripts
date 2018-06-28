import sys
from team_workspaces import list_workspace_access_verbose
from workspaces_api.workspaces import create_workspace_ids_list

workspace_id = str(sys.argv[1])
workspace_list = create_workspace_ids_list()

for workspace_access in list_workspace_access_verbose(workspace_list, workspace_id):
    print(workspace_access)