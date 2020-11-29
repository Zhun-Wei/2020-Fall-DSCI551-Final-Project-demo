import csv
import requests
import json

with open('sales.csv') as f:
    reader = csv.reader(f)
    result = list(reader)

sales_list = []
for i in range(len(result)):
    content = []
    for j in range(len(result[i])):
        content.append(result[i][j])
    sales_list.append(content)
print(sales_list[0])

sales_dict = {}
for i in range(1, len(sales_list)):
    info = {}
    for j in range(len(sales_list[i])):
        info[sales_list[0][j]] = sales_list[i][j]
    sales_dict[i] = info

print(sales_dict[493])

with open('sales.json', 'w') as f:
    json.dump(sales_dict, f)
sale_data = json.dumps(sales_dict)
# url1 = 'https://video-games-8113e.firebaseio.com/sales.json'
# response = requests.patch(url1, sale_data)
print('mission success')