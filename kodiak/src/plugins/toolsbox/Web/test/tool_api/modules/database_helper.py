
from .abs_database import ASBDatabase
from ..models.admin_finder_model import AdminFinderModel, DataBaseHandler

class DataBaseHelper(ASBDatabase):

    def __init__(self):
        super().__init__()
        DataBaseHandler().connect()

    def get_all(self):
        return [item.path for item in AdminFinderModel.select()]
