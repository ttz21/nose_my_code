#!/bin/sh
# Plugin needs to be installed first
nosetests --with-mycode
coverage run --source='.' test.py
