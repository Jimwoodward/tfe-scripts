import os
import sys
from workspace import create_workspace_ids_list
from workspace import list_workspace_ids

human_readable = sys.argv[1]
token = 'Bearer '+os.environ['TOKEN']
workspaces_list = create_workspace_ids_list(token)

for workspace_id in list_workspace_ids(token, human_readable, workspaces_list):
    print(workspace_id)
