#!/usr/bin/env python
"""
Reston
========

Reston is a reverse engine framework.

reverse android package and binary files.
---------------------------------------------

* DEX, ODEX
* APK
* Android's binary xml
* Disassemble DEX/ODEX bytecodes
* Decompiler for DEX/ODEX files

"""
import sys
import os

from setuptools import setup, find_packages

setup(
    name='reston',
    description='Reston is a reverse engine framwork, current can play with Android files.',
    long_description=__doc__,
    version='0.4',
    url='http://github.com/zeaphoo/reston/',
    packages=find_packages(),
    license='Apache',
    author='zeaphoo',
    author_email='zeaphoo@gmail.com',
    install_requires=['pyasn1', 'cryptography>=1.0', 'future', 'pygments'],
    setup_requires=['setuptools'],

)
