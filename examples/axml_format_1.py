#!/usr/bin/env python

from __future__ import print_function
import sys

PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from anguard.core.bytecodes import apk
from anguard.util import read

from xml.dom import minidom

ap = apk.AXMLPrinter(read("examples/axml/AndroidManifest2.xml", binary=False))

print(minidom.parseString(ap.getBuff()).toxml())
