import elasticsearch
import json

with open('flightdata.json') as data_file:
    airdata = json.load(data_file)

es = elasticsearch.Elasticsearch([{'host': '159.203.93.188', 'port': 9200}])

for i in range(len(airdata)):
    es.index(index='flights', doc_type='flight', id=i, body=airdata[i])
