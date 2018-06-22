import os
import sys
from workspace import list_workspace_access

workspace_id = str(sys.argv[1])
token = 'Bearer '+os.environ['TOKEN']

for workspace_access in list_workspace_access(token, workspace_id):
    print(workspace_access)
