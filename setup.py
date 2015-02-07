import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'my_code'
]

requires = []

setup(
    name='Nose My Code',
    version='0.0.1',
    description='Produces a colour coded nose stack trace',
    author='Hansel Dunlop, Jarek Dziedzic, Greg , Tina Zhang',
    author_email='aychedee@github.com, jarekdziedzic@github.com, arachnegl@github.com, ttz21@github.com',
    url='https://github.com/ttz21/nose_my_code',
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    license='BSD',
    zip_safe=False,
    entry_points = {
        'nose.plugins.0.10': [
            'colorize = my_code.traceback_hl:Colorize'
            ]
    }
)
