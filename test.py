"""
run with:
    nosetests test.py

"""
import unittest
import collections
import sys
import nose

from traceback_hl import HelloWorld


def calc():
    collections.OrderedDict('awef')


class TestHelloWorld(nose.plugins.PluginTester, unittest.TestCase):
    activate = '--hello'
    plugins = [HelloWorld()]

    def makeSuite(self):
        return unittest.TestSuite()

    def test_basic(self):
        try:
            calc()
        except Exception:
            traceback = sys.exc_traceback
            frame = traceback.tb_frame
            import ipdb; ipdb.set_trace()  # XXX BREAKPOINT
            self.assertTrue(hasattr(frame, 'f_lineno'))
            self.assertTrue(hasattr(frame, 'f_code'))
            code = frame.f_code
            self.assertTrue(hasattr(code, 'co_filename'))



from traceback_hl import HelloWorld

if __name__ == '__main__':
    nose.main(addplugins=[HelloWorld()])
