
from abc import abstractmethod


class ASBDatabase:

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_all(self):
        pass