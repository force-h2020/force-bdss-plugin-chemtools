#  (C) Copyright 2010-2020 Enthought, Inc., Austin, TX
#  All rights reserved.

import os
from setuptools import setup, find_packages

VERSION = "0.1.0.dev0"


# Read description
with open('README.rst', 'r') as readme:
    README_TEXT = readme.read()


def write_version_py():
    filename = os.path.join(
        os.path.dirname(__file__),
        'force_chemtools',
        'version.py')
    ver = "__version__ = '{}'\n"
    with open(filename, 'w') as fh:
        fh.write(ver.format(VERSION))


write_version_py()

setup(
    name="force_chemtools",
    version=VERSION,
    entry_points={
            "force.bdss.extensions": [
                "force_chemtools = "
                "force_chemtools.chemtools_plugin:ChemtoolsPlugin"
            ]
        },
    packages=find_packages(),
    install_requires=[
            "force_bdss >= 0.4.0",
        ]
)
