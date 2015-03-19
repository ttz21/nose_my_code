import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

execfile("mycode/__init__.py")


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'mycode'
]

requires = []

setup(
    name='nose-mycode',
    version=.__version__,
    description='Produces a colour coded nose stack trace',
    author='Hansel Dunlop, Jarek Dziedzic, Greg, Tina Zhang',
    author_email='aychedee@github.com, jarekdziedzic@github.com, arachnegl@github.com, ttz21@github.com',
    url='https://github.com/nose-my-code/nose-my-code',
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    license='BSD',
    zip_safe=False,
    entry_points = {
        'nose.plugins.0.10': [
            'mycode = mycode:MyCode'
            ]
    }
)
