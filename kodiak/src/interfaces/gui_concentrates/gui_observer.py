"""
    - created at 6/19/2020 by mjghasempour
    - this package is interface of observers that wanna path their values to other components
"""

from abc import ABC, abstractmethod


class GUIObserver(ABC):

    @abstractmethod
    def on_message(self, message: dict):
        pass

    @abstractmethod
    def class_name(self):
        pass
