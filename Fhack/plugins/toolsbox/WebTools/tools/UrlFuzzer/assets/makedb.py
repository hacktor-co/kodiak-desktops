
from os import getcwd

from peewee import (
    Model, CharField,
    SqliteDatabase
)


class DataBaseHelper:
    db_path = getcwd() + "/plugins/toolsbox/WebTools/tools/UrlFuzzer/assets/data.db"
    db_main = SqliteDatabase(db_path)

    def connect(self):
        self.db_main.connect()

    def close(self):
        self.db_main.close()


class LoginFinderModel(Model):
    path = CharField(max_length=512)
    language = CharField(max_length=100)

    class Meta:
        database = DataBaseHelper.db_main


def main():
    with open("", 'r') as file:
        for item in file.readlines():
            LoginFinderModel.create(path=item.strip("\n"), language="PHP").save()
            DataBaseHelper().close()


if __name__ == "__main__":
    main()
