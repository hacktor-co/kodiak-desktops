"""
    created at may 16/2020 by mjghasempour
    - this package is Services initializer of IoC
"""

from dependency_injector.containers import (
    DeclarativeContainer as DI_DeclarativeContainer
)
from dependency_injector.providers import (
    Callable as DI_Callable
)


class Application(DI_DeclarativeContainer):
    """ IoC container of application component providers. """

    def __init__(self):
        super(Application, self).__init__()

    def __run_app__(self):
        pass

    main: DI_Callable = DI_Callable(
        __run_app__, self=None
    )
