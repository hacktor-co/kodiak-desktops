"""
    - created at feb 03/2020 by mjghasempour
    - this package get configuration of servers and other things that thay are static from json file
        and then send value objects to top level
"""

from json import loads as json_loads

from easydict import EasyDict as edict


class ConfigManager:
    """ config manager class act as reading settings file and convert it to
        dictionary object
    """

    def __init__(self):
        super(ConfigManager, self).__init__()
        self._config_path: str = str()

    @property
    def config_path(self):
        return self._config_path

    @config_path.setter
    def config_path(self, config_path):
        self._config_path = config_path

    def __read_config__(self):
        if self._config_path != "":
            with open(self._config_path, 'r') as file:
                configs = json_loads(file.read().strip("\n"))
            return configs
        return None

    @property
    def get(self):
        return edict(self.__read_config__())
