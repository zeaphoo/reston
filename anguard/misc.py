from future import standard_library
standard_library.install_aliases()
from anguard.core import *
from anguard.core.bytecode import *
from anguard.core.bytecodes.dvm import *
from anguard.core.bytecodes.apk import *
from anguard.core.analysis.analysis import *
from anguard.decompiler.decompiler import *

from pickle import dumps, loads
from anguard.core import anconf


def init_print_colors():
    from IPython.utils import coloransi, io
    anconf.default_colors(coloransi.TermColors)
    CONF["PRINT_FCT"] = io.stdout.write


def save_session(l, filename):
    """
      save your session !

      :param l: a list of objects
      :type: a list of object
      :param filename: output filename to save the session
      :type filename: string

      :Example:
          save_session([a, vm, vmx], "msession.json")
  """
    with open(filename, "wb") as fd:
        fd.write(dumps(l, -1))


def load_session(filename):
    """
      load your session !

      :param filename: the filename where the session has been saved
      :type filename: string

      :rtype: the elements of your session :)

      :Example:
          a, vm, vmx = load_session("mysession.json")
  """
    return loads(read(filename, binary=False))


def AnalyzeAPK(filename, decompiler="dad", session=None):
    """
        Analyze an android application and setup all stuff for a more quickly analysis !

        :param filename: the filename of the android application or a buffer which represents the application
        :type filename: string
        :param decompiler: ded, dex2jad, dad (optional)
        :type decompiler: string

        :rtype: return the :class:`APK`, :class:`DalvikVMFormat`, and :class:`VMAnalysis` objects
    """
    anconf.debug("AnalyzeAPK")

    if not session:
        session = CONF["SESSION"]

    with open(filename, "rb") as fd:
        data = fd.read()

    session.add(filename, data)
    return session.get_objects_apk(filename)


def AnalyzeDex(filename, decompiler="dad", session=None):
    """
        Analyze an android dex file and setup all stuff for a more quickly analysis !

        :param filename: the filename of the android dex file or a buffer which represents the dex file
        :type filename: string

        :rtype: return the :class:`DalvikVMFormat`, and :class:`VMAnalysis` objects
    """
    anconf.debug("AnalyzeDex")

    if not session:
        session = CONF["SESSION"]

    with open(filename, "rb") as fd:
        data = fd.read()

    return session.addDEX(filename, data)


def AnalyzeODex(filename, decompiler="dad", session=None):
    """
        Analyze an android odex file and setup all stuff for a more quickly analysis !

        :param filename: the filename of the android dex file or a buffer which represents the dex file
        :type filename: string

        :rtype: return the :class:`DalvikOdexVMFormat`, and :class:`VMAnalysis` objects
    """
    anconf.debug("AnalyzeODex")

    if not session:
        session = CONF["SESSION"]

    with open(filename, "rb") as fd:
        data = fd.read()

    return session.addDEY(filename, data)


def RunDecompiler(d, dx, decompiler, session=None):
    """
        Run the decompiler on a specific analysis

        :param d: the DalvikVMFormat object
        :type d: :class:`DalvikVMFormat` object
        :param dx: the analysis of the format
        :type dx: :class:`VMAnalysis` object
        :param decompiler: the type of decompiler to use ("dad", "dex2jad", "ded")
        :type decompiler: string
    """
    if decompiler != None:
        anconf.debug("Decompiler ...")
        decompiler = decompiler.lower()
        if decompiler == "dex2jad":
            d.set_decompiler(DecompilerDex2Jad(
                d, anconf.CONF["PATH_DEX2JAR"], anconf.CONF["BIN_DEX2JAR"
                              ], anconf.CONF["PATH_JAD"],
                anconf.CONF["BIN_JAD"], anconf.CONF["TMP_DIRECTORY"]))
        elif decompiler == "dex2fernflower":
            d.set_decompiler(DecompilerDex2Fernflower(
                d, anconf.CONF["PATH_DEX2JAR"], anconf.CONF[
                    "BIN_DEX2JAR"
                ], anconf.CONF["PATH_FERNFLOWER"], anconf.CONF[
                    "BIN_FERNFLOWER"
                ], anconf.CONF["OPTIONS_FERNFLOWER"
                                 ], anconf.CONF["TMP_DIRECTORY"]))
        elif decompiler == "ded":
            d.set_decompiler(DecompilerDed(d, anconf.CONF["PATH_DED"],
                                           anconf.CONF["BIN_DED"],
                                           anconf.CONF["TMP_DIRECTORY"]))
        else:
            d.set_decompiler(DecompilerDAD(d, dx))