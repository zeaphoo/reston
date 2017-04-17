#!/usr/bin/env python
import sys
import os

from setuptools import setup, find_packages

setup(
    name='anguard',
    description='Anguard is a full python tool to play with Android files.',
    version='0.3',
    packages=find_packages(),
    install_requires=['pyasn1', 'cryptography>=1.0', 'future', 'pygments'],
    setup_requires=['setuptools'],

)
