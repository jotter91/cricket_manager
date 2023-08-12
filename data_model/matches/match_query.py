import json
import os

target_match = input('please enter the match you want to query (without extension): ') + '.json'
#64814

extracted_json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extracted', target_match)

with open(extracted_json_path, 'r') as json_file:
    data = json.load(json_file)

players = data['info']['players']
player_info = {}

for player, player_id in players.items():
    player_info[player] = {'runs_scored': 0, 'runs_given': 0, 'deliveries_faced': 0, 'deliveries_bowled': 0, 'team': None}

for team, player_list in players.items():
    for player in player_list:
        player_info[player] = {'runs_scored': 0, 'runs_given': 0, 'deliveries_faced': 0, 'deliveries_bowled': 0, 'team': team}


innings = data['innings']
for inning in innings:
    team = inning['team']
    overs = inning['overs']

    for over in overs:
        deliveries = over['deliveries']

        for delivery in deliveries:
            batter = delivery['batter']
            bowler = delivery['bowler']
            runs_scored = delivery['runs']['batter']
            extras = delivery['runs']['extras']
            runs_given = delivery['runs']['total'] - extras

            player_info[batter]['runs_scored'] += runs_scored
            player_info[bowler]['runs_given'] += runs_given

            if batter != bowler:
                player_info[batter]['deliveries_faced'] += 1
            player_info[bowler]['deliveries_bowled'] += 1

# Print player information
for player, info in player_info.items():
    print(f"Player: {player}")
    print(f"Team: {info['team']}")
    print(f"Runs Scored: {info['runs_scored']}")
    print(f"Deliveries Faced: {info['deliveries_faced']}")
    print(f"Runs Given: {info['runs_given']}")
    print(f"Deliveries Bowled: {info['deliveries_bowled']}")
    print("-" * 20)