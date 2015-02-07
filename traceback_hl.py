from nose.plugins import Plugin
import sys

class Colorize(Plugin):
    name = 'color'
    enabled = True

    def addError(self, test, err, capt):
        self.stream.write("colorized traceback (eventually): ")
        traceback = sys.exc_info()[2]
        # TODO: print only if it's the current file (test.py)
        frame = traceback.tb_frame
        filename = frame.f_code.co_filename
        self.stream.write("filename = ")
        self.stream.write(filename)


    def setOutputStream(self, stream):
        # grab for own use
        self.stream = stream
        # return dummy stream to suppress default output
        class dummy:
            def write(self, *arg):
                pass
            def writeln(self, *arg):
                pass
        d = dummy()
        return d


