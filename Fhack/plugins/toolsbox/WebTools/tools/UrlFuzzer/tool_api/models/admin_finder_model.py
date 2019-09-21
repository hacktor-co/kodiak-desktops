from peewee import (
    Model, CharField,
    DateField
)

from ..modules.database_handler import DataBaseHelper


class AdminFinderModel(Model):
    path = CharField(max_length=512)
    created = DateField()

    class Meta:
        dataabse = DataBaseHelper.db_main
