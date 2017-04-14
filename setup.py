#!/usr/bin/env python
import sys
import os

from setuptools import setup, find_packages

# TODO this is actually a hack... How to copy the files to the right folder?
#guidir = os.path.join(sys.prefix, 'Scripts', 'anguard', 'gui')
#if not os.path.isdir(guidir):
#    os.makedirs(guidir)

setup(
    name='anguard',
    description='Anguard is a full python tool to play with Android files.',
    version='3.0',
    packages=find_packages(),
    install_requires=['pyasn1', 'cryptography>=1.0', 'future', 'pygments'],
    extras_require={
        'docs': ['sphinx', 'sphinxcontrib-programoutput'],
        # If you are installing on debian, you can use python3-magic instead
        'magic': ['filemagic'],
        'graphing': ['pydot'],
    },
    setup_requires=['setuptools'],

)
