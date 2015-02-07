from nose.plugins import Plugin


class HelloWorld(Plugin):
    name = 'hello'

    def __init__(self):
        pass

    def options(self, parser, env):
        Plugin.options(self, parser, env)
        parser.add_option('--hello', action='store_true')

    def configure(self, options, config):
        self.enableOpt = 'hello'

        print self.enableOpt, type(self.enableOpt)
        if not self.enabled:
            return
        Plugin.configure(self, options, config)

    def finalize(self, result):
        raise(Exception())


