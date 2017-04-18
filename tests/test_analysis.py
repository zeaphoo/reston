from reston.core import dvm
from reston.core import analysis

def test_Dex():
    with open("tests/testdata/android/TestsReston/bin/classes.dex",
              "rb") as fd:
        d = dvm.DalvikVMFormat(fd.read())
        dx = analysis.Analysis(d)
        assert dx != None
