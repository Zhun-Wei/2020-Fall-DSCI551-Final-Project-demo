import csv
import requests
import json

with open('rating.csv') as f:
    reader = csv.reader(f)
    result = list(reader)

rating_list = []
for i in range(len(result)):
    content = []
    for j in range(len(result[i])):
        content.append(result[i][j])
    rating_list.append(content)
print(rating_list[0])

rating_dict = {}
for i in range(1, len(rating_list)):
    info = {}
    for j in range(len(rating_list[i])):
        info[rating_list[0][j]] = rating_list[i][j]
    rating_dict[i] = info

new_rating_dict = {}
for key in rating_dict:
    if rating_dict[key]['Critic_Score'] == '' or rating_dict[key]['User_Score'] == '':
        continue
    else:
        new_rating_dict[key] = rating_dict[key]
print(new_rating_dict)

with open('rating.json', 'w') as f:
    for i in new_rating_dict:
        json.dump(new_rating_dict[i], f)
rating_data = json.dumps(new_rating_dict)
# url1 = 'https://video-games-8113e.firebaseio.com/rating.json'
# response = requests.patch(url1, rating_data)
print('mission success')
