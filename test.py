import nose
import unittest

from mycode import MyCode

from collections import OrderedDict

from mycode import highlight_traceback, _red, _blue, _bold

def ouch():
    OrderedDict('ouch')


class MyCodeTest(unittest.TestCase):

    @unittest.skip('for manual testing')
    def test_output_is_highlighted(self):
        ouch()

    def test_highlight_traceback(self):

        cwd = '/Users/User/mycode'
        got = highlight_traceback(a_traceback, cwd)

        red_error = _red('ValueError: need more than 1 value to unpack')
        self.assertIn(red_error, got)

        blue_lines = blues.split('\n')
        for line in blue_lines:
            blue_line = _blue(line)
            self.assertIn(blue_line, got)

        bold_intro = _bold('Traceback (most recent call last):')
        self.assertIn(bold_intro, got)


blues = \
"""\
  File "/Users/User/mycode/test.py", line 20, in test_output_is_highlighted
    ouch()
  File "/Users/User/mycode/test.py", line 13, in ouch
    OrderedDict('ouch')"""


a_traceback = \
"""Traceback (most recent call last):
  File "/Users/User/mycode/test.py", line 20, in test_output_is_highlighted
    ouch()
  File "/Users/User/mycode/test.py", line 13, in ouch
    OrderedDict('ouch')
  File "/Users/User/.virtualenvs/dj-light/lib/python3.4/collections/__init__.py", line 56, in __init__
    self.__update(*args, **kwds)
  File "/Users/User/.virtualenvs/dj-light/bin/../lib/python3.4/_collections_abc.py", line 602, in update
    for key, value in other:
ValueError: need more than 1 value to unpack
"""

if __name__ == '__main__':
    nose.main(addplugins=[MyCode()])
