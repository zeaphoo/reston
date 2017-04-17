from anguard.core import dvm
from anguard.core import analysis

def test_Dex():
    with open("tests/testdata/android/TestsAnguard/bin/classes.dex",
              "rb") as fd:
        d = dvm.DalvikVMFormat(fd.read())
        dx = analysis.Analysis(d)
        assert dx != None
