from anguard.core import dvm

def test_dex():
    with open("tests/testdata/android/TestsAnguard/bin/classes.dex",
              "rb") as fd:
        d = dvm.DalvikVMFormat(fd.read())
        assert d != None

        classes = d.get_classes()
        assert classes != None
        assert len(classes) == 340

        methods = d.get_methods()
        assert methods != None
        assert len(methods) == 2600

        fields = d.get_fields()
        assert fields != None
        assert len(fields) == 803
