from nose.plugins import Plugin


class Colorize(Plugin):
    name = 'color'
    enabled = True

    def addError(self, test, err, capt):
        self.stream.write("colorized error: ")

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


