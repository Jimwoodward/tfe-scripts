from workspaces import create_workspace_ids_list, list_workspace_id

workspaces_list = create_workspace_ids_list()

for workspace_id in list_workspace_id(workspaces_list):
    print(workspace_id)
