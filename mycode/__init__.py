from nose.plugins import Plugin
import os

bold = '\033[1m{0}\033[0m'
red = "\033[1;31m{0}\033[00m"
green = "\033[1;32m{0}\033[00m"
blue = "\033[1;34m{0}\033[00m"


class HighlightedStream(object):

    def __init__(self, stream):
        self.stream = stream
        self.current_path = os.getcwd()

    def highlight_traceback_msg(self, msg):
        lines = msg.split('\n')

        # assumptions: A unit covers 2 lines so total always odd
        # 2 lines for each unit + 1 line for Traceback string
        assert len(lines) % 2 == 1

        # embolden traceback line
        intro_idx = 0
        lines[intro_idx] = bold.format(lines[intro_idx])

        # higlight mycode
        for i in range(1, len(lines[-2:]), 2):
            curr, next_ = i, i + 1
            line = lines[curr]
            if self.current_path in line:
                lines[curr] = blue.format(lines[curr])
                lines[next_] = blue.format(lines[next_])

        # red error mesage
        err_idx = -2
        lines[err_idx] = red.format(lines[err_idx])

        return '\n'.join(lines)

    def write(self, msg):
        if msg.startswith('Traceback'):
            msg = self.highlight_traceback_msg(msg)
            self.stream.write(msg)
        else:
            self.stream.write(msg)

    def writeln(self, arg=None):
        if arg:
            self.write(arg)
        self.write('\n')

    def flush(self):
        self.stream.flush()


class MyCode(Plugin):
    '''Highlights traceback lines that are in the current project.

    '''
    name = 'mycode'
    enabled = False
    score = 999

    def setOutputStream(self, stream):
        return HighlightedStream(stream)
