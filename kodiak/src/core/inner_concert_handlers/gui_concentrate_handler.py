"""
    - created at 6/19/2020 by mjghasempour
    - this package is gui observer handlers
"""

from interfaces.gui_concentrates.gui_subject import GUISubjects
from interfaces.gui_concentrates.gui_observer import GUIObserver

from typing import Set


class GUIConcentrateHandler(GUISubjects):
    """
        The Subject owns some important state and notifies inner_concentrate when the state
        changes.
    """
    def __init__(self):
        super(GUIConcentrateHandler, self).__init__()

        self.__observers__: Set[Observer] = set()

    def attach(self, observer: object):
        """ add new compenent class to this concentrate handler
        :param observer: child observer class
        :return: nothing
        """
        for item in self.__observers__:
            if item.class_name == observer.class_name:
                return
        self.__observers__.add(observer)

    def detach(self):
        self._observers.discard(observer)

    def notify(self, message: object, to: str):
        """ notify message to each componenet that has it
        :param message:
        :param to: message send to specified compoenent
        :return: nothing
        """
        for observer in self.__observers__:
            if observer.class_name == to:
                observer.on_message(message)

    def get_observers(self) -> set:
        """ get set of observer that attached to this hanlder
        :return: set of observers
        """
        return self.__observers__

    def get_class(self, class_name: str) -> object:
        """ get object of selected observer
        :param class_name: observer (class_name) name
        :return: object of created observer class
        """
        for item in self.__observers__:
            if item.__str__() == class_name:
                return item
