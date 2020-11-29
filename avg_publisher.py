from pyspark.sql import SparkSession
import pyspark.sql.functions as fc
import json
import requests

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("readCSV").getOrCreate()
rating = spark.read.csv('rating.csv', header=True)

publisher = rating.groupBy('Publisher').agg(fc.avg('User_score').alias('score'))
publisher = publisher.orderBy(fc.desc('score'))

df = publisher.toPandas()
df_js = df.to_json()
publisher_dict = json.loads(df_js)
result_dict = {}
for i in range(0, len(publisher_dict['Publisher'])):
    sub_dict = {}
    for j in publisher_dict.keys():
        if j == 'score' and publisher_dict[j][str(i)] is not None:
            publisher_dict[j][str(i)] = round(publisher_dict[j][str(i)], 2)
        sub_dict[j] = publisher_dict[j][str(i)]
    result_dict[i+1] = sub_dict

publisher_dict2 = {}
for i in result_dict:
    publisher_dict2[result_dict[i]['Publisher']] = result_dict[i]
print(publisher_dict2)

publisher_dict3 = publisher_dict2
for key in publisher_dict3:
    del publisher_dict3[key]['Publisher']

with open('publisher1.json', 'w') as f:
    f.write(str(publisher_dict3))
data = json.dumps(publisher_dict2)

url = 'https://video-games-8113e.firebaseio.com/publisher.json'
response = requests.patch(url, data)



print(publisher_dict2)

