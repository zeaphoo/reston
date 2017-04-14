#!/usr/bin/env python

from __future__ import print_function
from builtins import hex
import sys

PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from anguard.core.bytecodes import dvm
from anguard.core import anconf
from anguard.util import read

FILENAME_INPUT = "examples/android/TestsAnguard/bin/classes.dex"
FILENAME_OUTPUT = "./toto.dex"

anconf.set_debug()

vm = dvm.DalvikVMFormat(read(FILENAME_INPUT))

print(hex(vm.header.link_off), hex(vm.header.link_size))
vm.header.link_off, vm.header.link_size = 0x41414141, 0x1337
print(hex(vm.header.link_off), hex(vm.header.link_size))

new_dex = vm.save()

with open(FILENAME_OUTPUT, "wb") as fd:
    fd.write(new_dex)
