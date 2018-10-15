import csv
f = open("/dcs/pg18/u1897477/Downloads/football.csv","r")
goal_data = f.read()
goal_data = goal_data.split("\n")
goal_differences = []
team_names = []
for i in goal_data[1:]:
    row = i.split(",")
    goals_scored = int(row[5])
    goals_conceded = int(row[6])
    goal_differential = goals_scored - goals_conceded
    goal_differences.append(goal_differential)
for i in goal_data[1:]:
    x = i.split(",")
    team = x[0]
    team_names.append(team)
abs_differences = [abs(x) for x in goal_differences]
team_dictionary = dict(zip(team_names, abs_differences))
print(team_dictionary)
print(min(team_dictionary.items(), key=lambda x: x[1]))
print(max(team_dictionary.items(), key=lambda x: x[1]))
