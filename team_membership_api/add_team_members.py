import sys
from team_membership import add_team_member

team_id = str(sys.argv[1])
user_name = str(sys.argv[2])

for response in add_team_member(user_name, team_id):
    print(response)