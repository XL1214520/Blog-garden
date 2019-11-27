# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from Cnblogs.settings import mongo_host,mongo_port,mongo_db_name,mong_db_collection
import pymongo

class CnblogsPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mong_db_collection
        client = pymongo.MongoClient(host=host,port=port)

        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        self.post.update({'origin_url':item['origin_url']},{'$set':item},True)
        return item
