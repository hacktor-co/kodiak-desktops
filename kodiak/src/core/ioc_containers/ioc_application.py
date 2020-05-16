"""
    created at may 16/2020 by mjghasempour
    - this package is Services initializer of IoC
"""

from sys import argv, exit as sys_exit

from PyQt5.QtWidgets import QApplication
from dependency_injector.containers import (
    DeclarativeContainer as DI_DeclarativeContainer
)
from dependency_injector.providers import (
    Callable as DI_Callable
)

from gui.dasboard.main_window.main_window import DashboardMainWindow


class Application(DI_DeclarativeContainer):
    """ IoC container of application component providers. """

    def __init__(self):
        super(Application, self).__init__()

    def __run_app__(self):
        app = QApplication(argv)
        DashboardMainWindow()
        sys_exit(app.exec_())

    main: DI_Callable = DI_Callable(
        __run_app__, self=None
    )
