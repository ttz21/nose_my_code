import nose
import unittest

from mycode import MyCode

from collections import OrderedDict


def ouch():
    OrderedDict('ouch')


class MyCodeTest(unittest.TestCase):

    def test_output_is_highlighted(self):
        ouch()


if __name__ == '__main__':
    nose.main(addplugins=[MyCode()])
