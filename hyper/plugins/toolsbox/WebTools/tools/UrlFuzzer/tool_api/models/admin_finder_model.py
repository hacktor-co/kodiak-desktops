from peewee import (
    Model, CharField,
    DateField
)

from ..modules.database_handler import DataBaseHelper


class AdminFinderModel(Model):
    path = CharField(max_length=512)

    class Meta:
        database = DataBaseHelper.db_main
