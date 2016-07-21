"""
 Provides utilities for flatlib package development.

"""

import os
import shutil
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(BASE_DIR)
PKG_DIR = os.path.join(PROJ_DIR, 'flatlib')

sys.path.append(PROJ_DIR)


def clean_caches(path):
    """
    Removes all python cache files recursively on a path.

    :param path: the path
    :return: None
    """

    for dirname, subdirlist, filelist in os.walk(path):

        for f in filelist:
            if f.endswith('pyc'):
                try:
                    os.remove(os.path.join(dirname, f))
                except FileNotFoundError:
                    pass

        if dirname.endswith('__pycache__'):
            shutil.rmtree(dirname)


def clean_py_files(path):
    """
    Removes all .py files.

    :param path: the path
    :return: None
    """

    for dirname, subdirlist, filelist in os.walk(path):

        for f in filelist:
            if f.endswith('py'):
                os.remove(os.path.join(dirname, f))
