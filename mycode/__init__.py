from nose.plugins import Plugin
import os

_bold = lambda a_str: '\x1b[1m{0}\x1b[0m'.format(a_str)
_red =  lambda a_str: "\x1b[1;31m{0}\x1b[0m".format(a_str)
_blue = lambda a_str: "\x1b[1;34m{0}\x1b[0m".format(a_str)


def highlight_traceback(traceback, cwd):
    lines = traceback.split('\n')

    # embolden traceback line
    intro_idx = 0
    lines[intro_idx] = _bold(lines[intro_idx])

    # higlight mycode
    skip_next = False
    for i in range(1, len(lines[:-2])):
        if skip_next:
            skip_next = False
            continue
        curr, next_ = i, i + 1  # assumption: err lines always pair
        line = lines[curr]
        if cwd in line:
            lines[curr] = _blue(lines[curr])
            lines[next_] = _blue(lines[next_])
            skip_next = True

    # red error mesage
    err_idx = -2
    lines[err_idx] = _red(lines[err_idx])

    return '\n'.join(lines)


class HighlightedStream(object):

    def __init__(self, stream):
        self.stream = stream
        self.cwd = os.getcwd()

    def write(self, msg):
        if msg.startswith('Traceback'):
            msg = highlight_traceback(msg, self.cwd)
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
