#!/usr/bin/env python

import sys

PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from anguard.core.bytecodes import dvm
from anguard.core.analysis import analysis
from anguard.util import read

TEST = "examples/android/TestsAnguard/bin/classes.dex"

j = dvm.DalvikVMFormat(read(TEST, binary=False))
x = analysis.Analysis(j)
j.set_vmanalysis(x)

# SHOW CLASSES (verbose and pretty)
j.show()

# SHOW METHODS
for i in j.get_methods():
    i.pretty_show()
