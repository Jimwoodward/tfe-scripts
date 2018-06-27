from workspace import create_workspace_ids_list
from workspace import list_workspace_id

workspaces_list = create_workspace_ids_list()

for workspace_id in list_workspace_id(workspaces_list):
    print(workspace_id)
