from peewee import (
    Model, CharField,
    DateField
)

from ..modules.database_handler import DataBaseHandler


class AdminFinderModel(Model):
    path = CharField(max_length=512)

    class Meta:
        database = DataBaseHandler.db_main
