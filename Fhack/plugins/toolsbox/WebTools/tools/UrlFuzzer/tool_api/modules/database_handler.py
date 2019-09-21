
from peewee import SqliteDatabase

from os import getcwd


class DataBaseHelper:
    db_path = getcwd() + "/plugins/toolsbox/WebTools/tools/UrlFuzzer/assets/data.db"
    db_main = SqliteDatabase(db_path)

    def __init__(self):
        pass

    def connect(self):
        self.db_main.connect()

    def close(self):
        self.db_main.close()
