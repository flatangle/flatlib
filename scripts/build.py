"""
 Builds a compiled distribution of flatlib.

"""

import os
import shutil
import compileall

import utils


# Config
PKG_NAME = 'flatlib'
PKG_DIR = utils.PKG_DIR

BUILD_NAME = 'build'
BUILD_DIR = os.path.join(utils.PROJ_DIR, BUILD_NAME)
BUILD_DST = os.path.join(BUILD_DIR, PKG_NAME)

# Remove build/ directory
if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)

# Copy package to build
shutil.copytree(PKG_DIR, BUILD_DST)

# Clean cache files
utils.clean_caches(BUILD_DST)

# Create legacy pyc files
compileall.compile_dir(BUILD_DST, force=True, legacy=True, quiet=1)

# Remove .py files
utils.clean_py_files(BUILD_DST)

# Move resources to build path (we don't want resources inside the zip)
RES_SRC_DIR = os.path.join(BUILD_DST, 'resources')
RES_DST_DIR = os.path.join(BUILD_DIR, 'resources')
shutil.move(RES_SRC_DIR, RES_DST_DIR)

# Create zip file
import flatlib

VERSION = flatlib.__version__
zipname = '%s-%s' % (PKG_NAME, VERSION)
shutil.make_archive(os.path.join(BUILD_DIR, zipname), 'zip',
                    root_dir=BUILD_DIR, base_dir=PKG_NAME)

# Copy resources back
shutil.copytree(RES_DST_DIR, RES_SRC_DIR)
