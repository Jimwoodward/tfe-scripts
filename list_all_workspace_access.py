import os
from workspace import list_workspace_access
from workspace import list_workspace_ids

token = 'Bearer '+os.environ['TOKEN']

for workspace_id in list_workspace_ids(token, 'False'):
    for results in list_workspace_access(token, workspace_id, 'True'):
        print(results)
