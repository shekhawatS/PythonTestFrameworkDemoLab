# -*- coding: UTF-8 -*
"""
Setup script for behave.example

USAGE:
    python setup.py install
    python setup.py behave_test     # -- XFAIL on Windows (currently).
"""

import sys
import os.path

HERE0 = os.path.dirname(__file__) or os.curdir
os.chdir(HERE0)
HERE = os.curdir
sys.path.insert(0, os.path.abspath(HERE))

from setuptools import find_packages, setup
# -- PREPARED: from setuptools_behave import behave_test


# -----------------------------------------------------------------------------
# CONFIGURATION:
# -----------------------------------------------------------------------------
description = """\
Some tutorials and examples to explore behave, a BDD test tool for Python.
"""
# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
setup(
    name="behave tests",
    version="1.0",
    license="BSD",
    description= description,
    keywords   = "utility",
    platforms  = [ 'any' ],
    # -- REQUIREMENTS:
    # SUPPORT: python2.7, python3.3 (or higher)
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
    install_requires=[
        "behave>=1.2.6",
        # -- BEHAVE EXAMPLES REQUIRE:
        "PyHamcrest>=1.9",
        "parse>=1.8.2",
        "parse_type>=0.4.2",
        "six>=1.11.0",
    ]
)
