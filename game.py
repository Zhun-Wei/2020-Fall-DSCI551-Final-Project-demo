import csv
import requests
import json

with open('game.csv') as f:
    reader = csv.reader(f)
    result = list(reader)

game_list = []
for i in range(len(result)):
    content = []
    for j in range(len(result[i])):
        content.append(result[i][j])
    game_list.append(content)
print(game_list[0])

game_dict = {}
for i in range(1, len(game_list)):
    info = {}
    for j in range(len(game_list[i])):
        info[game_list[0][j]] = game_list[i][j]
    game_dict[i] = info

print(game_dict[493])
game_str = ''
with open('games.json', 'w') as f:
    for i in game_dict:
        game_str = game_str + str(game_dict[i]) + ','
    f.write(game_str[:-1])
game_data = json.dumps(game_dict)
# url1 = 'https://video-games-8113e.firebaseio.com/games.json'
# response = requests.patch(url1, game_data)
print('mission success')