"""
    - this file created at 27 Jul/2019
    - author: hacktorco
    - this package handle working with file and directory
"""

import os

GET_CWD = os.getcwd()  # current working directory

def get_all_directory(path):
    list_of_dir = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        for dirs in dirnames:
            list_of_dir.append(dirs)
    return list_of_dir

