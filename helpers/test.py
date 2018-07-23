import sys
from helpers import team_workspace_access_generator

team_id = sys.argv[1]

team_workspace_access_generator(team_id, 'admin')