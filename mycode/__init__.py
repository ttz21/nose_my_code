from nose.plugins import Plugin
import os

bold = '\033[1m{0}\033[0m'
red = "\033[01;31m{0}\033[00m"
green = "\033[1;36m{0}\033[00m"
blue = "\033[1;34m{0}\033[00m"


class HighlightedStream(object):

    def __init__(self, stream):
        self.stream = stream
        self.current_path = os.getcwd()
        self.highlight_next = False

    def highlight(self, line):
        if self.current_path in line or self.highlight_next:
            self.highlight_next = not self.highlight_next
            return blue.format(line)
        return line

    def write(self, msg):
        self.stream.write(
            '\n'.join([self.highlight(line) for line in msg.split('\n')]))

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
