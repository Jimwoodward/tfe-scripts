import sys
from teams import list_team_members

team_id = str(sys.argv[1])

for team_member in list_team_members(team_id):
    print(team_member)
