#!/usr/bin/env python

from __future__ import print_function
import sys

PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from anguard.core.bytecodes import dvm
from anguard.core.analysis import analysis
from anguard.decompiler.dad import decompile
from anguard.util import read

TEST = 'examples/android/TestsAnguard/bin/classes.dex'

vm = dvm.DalvikVMFormat(read(TEST, binary=False))
vmx = analysis.VMAnalysis(vm)

# CFG
for method in vm.get_methods():
    mx = vmx.get_method(method)

    if method.get_code() == None:
        continue

    print(method.get_class_name(), method.get_name(), method.get_descriptor())

    ms = decompile.DvMethod(mx)
    ms.process()

    print(ms.get_source())
