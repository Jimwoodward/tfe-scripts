import os
import sys
from workspace import list_workspace_access

workspace_id = str(sys.argv[1])
human_readable = str(sys.argv[2])
token = 'Bearer '+os.environ['TOKEN']
lists = []

for workspace_access in list_workspace_access(token, workspace_id, human_readable, lists):
    print(workspace_access)
