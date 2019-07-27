"""
    - this file created at 27 Jul/2019
    - All rights reserved for hacktor team

    - this package handle working with file and directory
"""

import os

GET_CWD = os.getcwd()  # current working directory

def get_all_directory(path, level: int = 0) -> list:
    """
    get all directory that exist in path
    :param path: directory path
    :param level: depth of crawling
    :return: list of directories
    """
    some_dir = path.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)

    list_dirs = list()

    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        for item in dirs:
            list_dirs.append(item)
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]
    list_dirs.sort(reverse=True)

    return list_dirs
