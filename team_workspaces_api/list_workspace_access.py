import sys
from team_workspaces import list_workspace_access

workspace_id = str(sys.argv[1])

for workspace_access in list_workspace_access(workspace_id):
    print(workspace_access)
