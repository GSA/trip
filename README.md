# TRIP (GSA Hackathon)
## Travel Registration Info Portal

This is code for creating Kibana dashboards for information from the Reservation Air Data set:

Example dashboard [here](http://trip-gsa-hackathon.us:5601/#/dashboard/Flights-Departing-from-a-Given-Airport?_a=(filters:!(),panels:!((col:1,id:advance-purchase-count-histogram,row:7,size_x:9,size_y:3,type:visualization),(col:1,id:advance-purchase-total-cost-histogram,row:10,size_x:9,size_y:3,type:visualization),(col:7,id:destination-city-total-cost,row:1,size_x:6,size_y:6,type:visualization),(col:1,id:Airline-count,row:18,size_x:6,size_y:4,type:visualization),(col:7,id:Airline-total-amount,row:18,size_x:6,size_y:4,type:visualization),(col:10,id:Average-Total-Amount,row:7,size_x:3,size_y:2,type:visualization),(col:10,id:Top-Ten-Destination-coded-by-Average-amount,row:9,size_x:3,size_y:4,type:visualization),(col:1,id:destination-code-count-v2,row:1,size_x:6,size_y:6,type:visualization),(col:1,id:Online-or-not-questionmark-,row:13,size_x:6,size_y:5,type:visualization),(col:7,id:Fare-category,row:13,size_x:6,size_y:5,type:visualization)),query:(query_string:(analyze_wildcard:!t,query:'Origin_City_Code:%22DEN%22%20AND%20Agency:%22Agency%20A%22')),title:'Flights%20Departing%20from%20a%20Given%20Airport')&_g=())

To build a dashboard like this, first tell elastic search not to analyze text fields:

    sh create_index.sh

Then post the data in flightdata.json to elastic search

    python elasticpost.py

This tool was created by

Lamia Elgouacem - l.elgouacem@gmail.com

Ren C'deBaca - rectheworld@gmail.com

Damiano Melcarne - damianony@optonline.net

Evan Sonderegger - evan.sonderegger@gmail.com
