
from os import getcwd

from peewee import (
    Model, CharField,
    SqliteDatabase
)


class DataBaseHelper:
    db_path = "data.db"
    db_main = SqliteDatabase(db_path)

    def connect(self):
        self.db_main.connect()

    def close(self):
        self.db_main.close()


class AdminFinderModel(Model):
    path = CharField(max_length=512)

    class Meta:
        database = DataBaseHelper.db_main


def main():

    with open("./statics/admin-finder-urls-php.txt", 'r') as file:
        DataBaseHelper().connect()
        AdminFinderModel.create_table(safe=True)
        for item in file.readlines():
            AdminFinderModel.create(path=item.strip("\n")).save()
    DataBaseHelper().close()


if __name__ == "__main__":
    main()
