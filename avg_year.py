from pyspark.sql import SparkSession
import pyspark.sql.functions as fc
import json
import requests

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("readCSV").getOrCreate()
rating = spark.read.csv('rating.csv', header=True)

year = rating.groupBy('Year_of_Release').agg(fc.avg('User_score').alias('score'))
year = year.orderBy(fc.desc('score'))

df = year.toPandas()
df_js = df.to_json()
year_dict = json.loads(df_js)
result_dict = {}
for i in range(0, len(year_dict['Year_of_Release'])):
    sub_dict = {}
    for j in year_dict.keys():
        if j == 'score' and year_dict[j][str(i)] is not None:
            year_dict[j][str(i)] = round(year_dict[j][str(i)], 2)
        sub_dict[j] = year_dict[j][str(i)]
    result_dict[i+1] = sub_dict

year_dict2 = {}
for i in result_dict:
    year_dict2[result_dict[i]['Year_of_Release']] = result_dict[i]

year_list = []
year_dict3 = {}
year_dict4 = year_dict2
for key in year_dict4:
    del year_dict4[key]['Year_of_Release']
with open('year2.json', 'w') as f:
    # for i in year_dict2:
    #     year_list.append(year_dict2[i])
    # year_dict3['years'] = year_list
    f.write(json.dumps(year_dict2))
data = json.dumps(year_dict2)

url = 'https://video-games-8113e.firebaseio.com/year.json'
response = requests.patch(url, data)


print(year_dict2)

