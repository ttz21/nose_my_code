import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass
from setuptools import setup

setup(
    name='Colorize',
    version='0.1',
    description = 'Colorize output',
    py_modules = ['traceback_hl'],
    entry_points = {
        'nose.plugins': [
            'traceback_hl = traceback_hl:Colorize'
            ]
        }

    )