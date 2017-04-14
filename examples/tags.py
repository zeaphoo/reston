#!/usr/bin/env python

from __future__ import print_function
import sys

PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from anguard.core.bytecodes import dvm
from anguard.core.bytecodes import apk
from anguard.core.analysis import analysis
from anguard.core import anconf

import hashlib

TEST = "examples/android/TestsAnguard/bin/TestsAnguard.apk"

anconf.set_debug()

a = apk.APK(TEST)
vm = dvm.DalvikVMFormat(a.get_dex())
vmx = analysis.VMAnalysis(vm)

for i in vmx.get_methods():
    i.create_tags()

    tags = i.get_tags()
    if not tags.empty():
        print(tags)
