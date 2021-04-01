"""
    - Created on Aug 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - tool for finding directory of web applications
"""

import requests
from os import path

from .common.constants import WEB_HEADERS
from .modules.database_helper import DataBaseHelper

requests.packages.urllib3.disable_warnings()


def start_test_with_local_db(rhost: str):

    if rhost.endswith("/") is False:
        rhost = rhost + "/"

    for item in DataBaseHelper().get_all():
        url_directory = rhost + item

        response_code = requests.get(
            url=url_directory, headers=WEB_HEADERS,
            verify=False
        ).status_code

        yield ({
            "code": response_code,
            "url": url_directory
        })


def start_test_with_import_dict(rhost: str, file_path: str):
    if rhost.endswith("/") is False:
        rhost = rhost + "/"

    if path.exists(file_path) is not True:
        yield "path not exists"
        return
    if path.exists(file_path) and path.isdir(file_path):
        yield "path is directory"
        return

    with open(file_path, 'r') as file:
        for item in file.readlines():
            url_directory = rhost + item.strip("\n")

            response_code = requests.get(
                url=url_directory, headers=WEB_HEADERS,
                verify=False
            ).status_code

            yield ({
                "code": response_code,
                "url": url_directory
            })


def check_rhost(rhost: str) -> bool:
    """
        in this function first we check web site which is online or not
        then show menu to start
    :return:
    """
    try:

        response = requests.get(
            url=rhost, headers=WEB_HEADERS,
            verify=False, allow_redirects=False
        )
        if response.status_code == 200:
            return True
        else:
            return False

    except Exception:
        return False


def main_handler(rhost: str, import_file_path: str = None, use_local_database: bool = False):
    """

    :param rhost:
    :param import_file_path:
    :param use_local_database:
    :return:
    """

    is_rhost_up = False
    if check_rhost(rhost) is True:
        is_rhost_up = True
        yield ({
            "result": "rhost set successfully"
        })
    else:
        yield ({
            "result": "something is wrong with rhost please check it"
        })

    if is_rhost_up:
        if import_file_path is not None:
            for item in start_test_with_import_dict(rhost, import_file_path):
                yield ({
                    "result": item
                })

        elif use_local_database is True:
            for item in start_test_with_local_db(rhost):
                yield ({
                    "result": item
                })

    else:
        return
