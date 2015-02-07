"""
run with:
    nosetests test.py


"""
import unittest
import collections
import sys
import nose


def calc():
    collections.OrderedDict('awef')


class MyTest(unittest.TestCase):

    def test_basic(self):
        try:
            calc()
        except Exception as exc:
            traceback = sys.exc_traceback
            frame = traceback.tb_frame
            self.assertTrue(hasattr(frame, 'f_lineno'))
            self.assertTrue(hasattr(frame, 'f_code'))
            code = frame.f_code
            self.assertTrue(hasattr(code, 'co_filename'))


if __name__ == '__main__':
    nose.main()
