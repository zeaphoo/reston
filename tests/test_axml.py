import unittest

import sys
PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from anguard.core.bytecodes import apk


class AXMLTest(unittest.TestCase):

    def testAXML(self):
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
                self.assertTrue(ap)


if __name__ == '__main__':
    unittest.main()
