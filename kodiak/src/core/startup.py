"""
    - Created on May 13/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package start application an initialize all component and
        dependencies
"""

from .ioc_containers.ioc_application import Application


class StartUp:
    
    def __init__(self):
        super(StartUp, self).__init__()

    def start_app(self):
        Application.main()

