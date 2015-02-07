import logging
import os

from nose.plugins import Plugin
from nose.plugins import PluginTester


class HelloWorld(Plugin):
    name = 'hi'

    def __init__(self):
        raise(Exception())

    def options(self, parser, env=os.environ):
        parser.add_options('--hi', action='store_true')
        Plugin.options(self, parser, env=env)


    def configure(self, options, conf):
        super(HelloWorld, self).configure(options, conf)
        if not self.enabled:
            return

    def finalize(self, result):
        raise(Exception())


