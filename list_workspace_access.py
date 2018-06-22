import os
import sys
from workspace import list_workspace_access

workspace_id = str(sys.argv[1])
human_readable = str(sys.argv[2])
token = 'Bearer '+os.environ['TOKEN']

for workspace_access in list_workspace_access(token, workspace_id, human_readable):
    print(workspace_access)
