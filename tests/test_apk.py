import unittest

import sys

from reston.core import apk

import os


def test_apk():
    print os.getcwd()
    with open("tests/testdata/android/TestsReston/bin/TestActivity.apk",
              "rb") as fd:
        a = apk.APK(fd.read(), True)
        assert a != None
