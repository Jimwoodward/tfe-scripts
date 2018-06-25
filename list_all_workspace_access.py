import os
import time
from workspace import list_workspace_access
from workspace import list_workspace_ids

token = 'Bearer '+os.environ['TOKEN']

begin = time.time()
for workspace_id in list_workspace_ids(token, 'False'):
    for results in list_workspace_access(token, workspace_id, 'False'):
        print(results)

end = time.time()
print(end - begin)
