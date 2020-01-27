import datetime
from elasticsearch import Elasticsearch
import json
from src.elasticmanager.logger import Logger


class ElasticLogger(Logger):

    elastic = None

    def __init__(self):
        self.indexname = "thermallogs"
        self.elastic = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    @staticmethod
    def __datedump__(d):
        if isinstance(d, datetime.datetime):
            return d.__str__()

    def write(self, obj):
        self.elastic.index(index=self.indexname,
                           doc_type="thermallog", body=json.dumps(obj.__dict__, default=self.__datedump__))



