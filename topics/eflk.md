## ELK + Filebeat

Set up the following using any log you would like:

* Run the following: elasticsearch, logstash, kibana and filebeat (each running in its own container)
* Make filebeat transfer a log to logstash for process
* Once logstash is done, index with elasticsearch
* Finally, make sure data is available in Kibana
