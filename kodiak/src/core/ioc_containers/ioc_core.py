"""
    created at may 16/2020 by mjghasempour
    - this package is core of IOC for config handlers and other critical configs
"""

from dependency_injector.containers import (
    DeclarativeContainer as DI_DeclarativeContainer
)
from dependency_injector.providers import (
    Singleton as DI_provider_singleton
)

from ..inner_concert_handlers.gui_concentrate_handler import GUIConcentrateHandler


class Core(DI_DeclarativeContainer):
    """ IoC container of core component providers.
            here we initialize the configs and other core options like logger or ...
    """

    gui_concentrate_handler = DI_provider_singleton(GUIConcentrateHandler)
