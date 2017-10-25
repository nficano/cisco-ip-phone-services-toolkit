#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from setuptools import setup, find_packages
from os import path
from ast import parse

try:
    # Python2
    from future_builtins import filter
except ImportError:
    # Python3
    pass

with open('README.rst') as license_file:
    readme = license_file.read()

with open('LICENSE.txt') as license_file:
    license = license_file.read()

with open(path.join('ciscoipphone', '__init__.py')) as f:
    __version__ = parse(next(filter(
        lambda line: line.startswith('__version__'), f))).body[0].value.s

setup(
    name='ciscoipphone',
    author='Nick Ficano',
    author_email='nficano@gmail.com',
    version=__version__,
    packages=find_packages(exclude=['tests*']),
    url='http://nickficano.com',
    description=("a collection of tools and constructor for quickly "
                 "generating and deploying Cisco IP phone directory "
                 "services."),
    zip_safe=False,
    long_description=readme,
    install_requires=['six'],
    license=license,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
    ]
)
