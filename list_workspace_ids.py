import os
import sys
from workspace import list_workspace_ids

human_readable = sys.argv[1]
token = 'Bearer '+os.environ['TOKEN']

list_workspace_ids(token, human_readable)
