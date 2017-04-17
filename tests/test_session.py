
from anguard import session


def test_SessionDex():
    s = session.Session()
    with open("tests/testdata/android/TestsAnguard/bin/classes.dex",
              "rb") as fd:
        s.add("tests/testdata/android/TestsAnguard/bin/classes.dex", fd.read())
        assert len(s.analyzed_apk) == 0
        assert len(s.analyzed_files) == 1
        assert len(s.analyzed_digest) == 1
        assert len(s.analyzed_dex) == 1

def test_SessionAPK():
    s = session.Session()
    with open("tests/testdata/android/TestsAnguard/bin/TestActivity.apk",
              "rb") as fd:
        s.add("tests/testdata/android/TestsAnguard/bin/TestActivity.apk",
              fd.read())
        assert len(s.analyzed_apk) == 1
        assert len(s.analyzed_files) == 1
        assert len(s.analyzed_digest) == 2
        assert len(s.analyzed_dex) == 1

def test_SessionSave():
    s = session.Session()
    with open("tests/testdata/android/TestsAnguard/bin/TestActivity.apk",
              "rb") as fd:
        s.add("tests/testdata/android/TestsAnguard/bin/TestActivity.apk",
              fd.read())
        session.Save(s, "test_session")
