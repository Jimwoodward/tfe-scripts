import os
import sys
from workspace import list_workspace_ids

human_readable = sys.argv[1]
token = 'Bearer '+os.environ['TOKEN']

for workspace_id in list_workspace_ids(token, human_readable):
    print(workspace_id)
