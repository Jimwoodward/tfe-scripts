import sys
import os
from workspace import list_workspace_access
from workspace import list_workspace_ids

human_readable = sys.argv[1]
token = 'Bearer '+os.environ['TOKEN']

for workspace_id in list_workspace_ids(token, False):
    list_workspace_access(token, workspace_id)
