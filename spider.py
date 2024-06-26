# encoding:utf-8
import os

import requests
import time
import threading
import logging
from loguru import  logger
import inspect,pymongo
import arrow
from dotenv import load_dotenv

load_dotenv()

class MongoHandler(logging.Handler):
    # 单例模式，确保每次实例化都调用一个对象。
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(MongoHandler, "_instance"):
            with MongoHandler._instance_lock:
                MongoHandler._instance = object.__new__(cls)
                return MongoHandler._instance

        return MongoHandler._instance

    def __init__(self, client, db=None, collection=None):
        super().__init__()
        self.client = client
        self.db = db
        self.collection = collection

    def emit(self, record):
        log_record = {
            "level": record.levelname,
            "timestamp": record.created,
            "message": self.format(record),
            "file": record.filename,
            "line": record.lineno,
        }
        if not self.db:
            self.db = record.extra.get("db")
        if not self.collection:
            self.collection = record.extra.get("collection")
        self.client[self.db][self.collection].insert_one(log_record)


class MongoLog(MongoHandler):
    def __init__(self, db='kol'):
        # 写死数据库和Mongo连接信息，日志存储在同名文集合下。比如b.py继承这个class ，那么集合名为b
        collection = 'log_' + os.path.basename(inspect.stack()[1].filename).split(".")[0]
        client = pymongo.MongoClient(f'mongodb://admin:pwd@139.9:27017/')
        super().__init__(client, db, collection)
        logger.add(self)
        self.log = logger

    def __call__(self, *args, **kwargs):
        return self.log

# my_log = MongoLog()()
# my_log.info(str(int(time.time())))
today = arrow.now().format('YYYY-MM-DD')

# Print the message with today's date
print(f'fxx my job {today}  test now for    harbor  ')
print(os.getenv("MONGO_PORT"))
