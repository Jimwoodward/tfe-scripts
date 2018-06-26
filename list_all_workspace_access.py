import os
import time
from workspace import create_workspace_ids_list
from workspace import list_workspace_access
from workspace import list_workspace_ids

token = 'Bearer '+os.environ['TOKEN']
workspaces_list = create_workspace_ids_list(token)

begin = time.time()
for workspace_id in list_workspace_ids(token, 'False', workspaces_list):
    for results in list_workspace_access(token, workspace_id, 'True', workspaces_list):
        print(results)

end = time.time()
print(end - begin)
