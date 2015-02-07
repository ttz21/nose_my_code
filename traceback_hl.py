from nose.plugins import Plugin


class Colorize(Plugin):
    name = 'color'
    enabled_for_errors = True
    enabled_for_failures = False
    score = 1 # run last, among builtins

    def options(self, parser, env):
        Plugin.options(self, parser, env)
        parser.add_option('--color', action='store_true')

    def configure(self, options, config):
        self.enableOpt = 'color'

        print self.enableOpt, type(self.enableOpt)
        if not self.enabled:
            return
        Plugin.configure(self, options, config)

    def formatError(test, err):
        import ipdb; ipdb.set_trace()  # XXX BREAKPOINT

    def handleError(test, err):
        import ipdb; ipdb.set_trace()  # XXX BREAKPOINT


    def finalize(self, result):
        raise(Exception())

    def addError(self, test, err, capt=None):
        print('COLOR PLUGIN')
        print(str(err))
