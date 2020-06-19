"""
    - created at feb 3/2020 by mjghasempour
    - this package get configuration of servers and other things that thay are static from json file
        and then send value objects to top level
"""

import functools


def singleton(class_):
    class class_w(class_):
        _instance = None
        _sealed: bool = False

        def __new__(cls, *args, **kwargs):

            if class_w._instance is None:
                class_w._instance = super(class_w, cls).__new__(cls, *args, **kwargs)
                class_w._instance._sealed = False

            return class_w._instance

        def __init__(self, *args, **kwargs):

            if self._sealed:
                return

            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True

    class_w.__name__ = class_.__name__
    return class_w
