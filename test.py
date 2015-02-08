"""
run with:
    nosetests test.py

"""
import unittest
import collections
import sys
import os
from termcolor import colored


PATHS = os.listdir(os.getcwd())

def calc():
    collections.OrderedDict('awef')


def is_in_paths(frame):
    for p in PATHS:
        if p in frame:
            return True
    return False


class ColorizeResult(unittest.TextTestResult):

    def _exc_info_to_string(self, err, test):
        msgLines = super(ColorizeResult, self)._exc_info_to_string(err, test)
        frames = msgLines.split('\n')

        out = []
        for frame in frames:
            if is_in_paths(frame):
                out.append(colored(frame, 'green'))
            else:
                out.append(frame)

        return '\n'.join(out)


class ColorizeRunner(unittest.TextTestRunner):
    resultclass = ColorizeResult


class TestHelloWorld(unittest.TestCase):

    def test_basic(self):
        try:
            calc()
        except Exception:
            traceback = sys.exc_traceback
            frame = traceback.tb_frame
            self.assertTrue(hasattr(frame, 'f_lineno'))
            self.assertTrue(hasattr(frame, 'f_code'))
            code = frame.f_code
            self.assertTrue(hasattr(code, 'co_filename'))

    def test_simple(self):
        calc()




if __name__ == '__main__':
    unittest.TestProgram(testRunner=ColorizeRunner)
    #unittest.main()
