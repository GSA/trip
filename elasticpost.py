import elasticsearch
import json

with open('airdata4.json') as data_file:
    airdata = json.load(data_file)

es = elasticsearch.Elasticsearch([{'host': '159.203.93.188', 'port': 9200}])

for i in range(len(airdata)):
    # print airdata[i]['Agency']
    es.index(index='flights', doc_type='flight', id=i, body=airdata[i])
