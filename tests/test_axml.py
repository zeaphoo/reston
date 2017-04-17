from anguard.core import apk

def test_AXML():
    filenames = [
        "tests/testdata/axml/AndroidManifest-Chinese.xml",
        "tests/testdata/axml/AndroidManifest-xmlns.xml",
        "tests/testdata/axml/AndroidManifest.xml", "tests/testdata/axml/test.xml",
        "tests/testdata/axml/test1.xml", "tests/testdata/axml/test2.xml",
        "tests/testdata/axml/test3.xml"
    ]

    for filename in filenames:
        with open(filename, "rb") as fd:
            ap = apk.AXMLPrinter(fd.read())
            assert ap != None
