"""
    created at may 16/2020 by mjghasempour
    - this package is core of IOC for config handlers and other critical configs
"""

from dependency_injector.containers import (
    DeclarativeContainer as DI_DeclarativeContainer
)


class Core(DI_DeclarativeContainer):
    """ IoC container of core component providers.
            here we initialize the configs and other core options like logger or ...
    """

    pass
