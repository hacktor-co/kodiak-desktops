"""
    - created at 6/19/2020 by mjghasempour
    - this package is interface of subjects that handle thier own observers
"""

from abc import ABC, abstractmethod


class GUISubjects(ABC):
    """
        the subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: object):
        """ Attach an observer to the subject """
        pass

    @abstractmethod
    def detach(self):
        """ Detach an observer from the subject. """
        pass

    @abstractmethod
    def notify(self, message: object, to: str):
        """ Notify all inner_concentrate about an event. """
        pass

    @abstractmethod
    def get_observers(self) -> set:
        """ get all observers that attached to main concentrate """
        pass

    @abstractmethod
    def get_class(self, class_name: str) -> object:
        """ get object of class that programmer enter it name to this method """
        pass
