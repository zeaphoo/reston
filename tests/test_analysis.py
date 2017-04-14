import unittest

import sys
PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from anguard.core.bytecodes import dvm
from anguard.core.analysis import analysis


class AnalysisTest(unittest.TestCase):

    def testDex(self):
        with open("tests/testdata/android/TestsAnguard/bin/classes.dex",
                  "rb") as fd:
            d = dvm.DalvikVMFormat(fd.read())
            dx = analysis.Analysis(d)
            self.assertTrue(dx)


if __name__ == '__main__':
    unittest.main()
