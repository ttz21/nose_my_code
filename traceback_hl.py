from nose.plugins import Plugin


class Colorize(Plugin):
    name = 'color'

    def options(self, parser, env):
        Plugin.options(self, parser, env)
        parser.add_option('--color', action='store_true')

    def configure(self, options, config):
        self.enableOpt = 'color'

        print self.enableOpt, type(self.enableOpt)
        if not self.enabled:
            return
        Plugin.configure(self, options, config)

    def finalize(self, result):
        raise(Exception())


