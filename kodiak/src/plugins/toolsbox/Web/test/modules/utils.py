"""
    - Created on 10/31/2019 - hacktorco
    - All rights reserved for hacktor team

    - This get all information and all config for specific OS
"""

from platform import system, release
from os import name as osname


def get_os_info():
    """
    get current OS information that application run on it
    :return: current system information
    """

    return {
        "os": str(system()),
        "release": str(release()),
        "name": osname
    }