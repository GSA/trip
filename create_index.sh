curl -XPUT trip-gsa-hackathon.us:9200/flights -d '{
        "mappings": {
            "flight": {
                "dynamic_templates": [
                    { "notanalyzed": {
                        "match":              "*",
                        "match_mapping_type": "string",
                        "mapping": {
                            "type":        "string",
                            "index":       "not_analyzed"
                            }
                        }
                    }
                ]
            }
        }
    }'
