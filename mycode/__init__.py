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
        self.highlight_next = False

    def highlight_blue(self, line):
        if self.current_path in line or self.highlight_next:
            self.highlight_next = not self.highlight_next
            return blue.format(line)
        return line

    def highlight_traceback_msg(self, msg):
        lines = msg.split('\n')
        # assumptions: A unit covers 2 lines so total always odd
        # 2 lines for each unit + 1 line for Traceback string
        assert len(lines) % 2 == 1
        intro_idx = 0
        lines[intro_idx] = bold.format(lines[intro_idx])
        for i in range(len(lines)):
            lines[i] = self.highlight_blue(lines[i])
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

    def options(self, parser, env):
        super(MyCode, self).options(parser, env=env)

    def configure(self, options, conf):
        super(MyCode, self).configure(options, conf)

    def setOutputStream(self, stream):
        return HighlightedStream(stream)
