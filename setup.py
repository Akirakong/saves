# coding:utf-8

import sys
from setuptools import setup

sys.path.append('./saves')
sys.path.append('./tests')

setup(
    name='saves',
    version='0.0.1.3',
    description='simple data persistence package.',
    url="https://github.com/Akirakong/saves",
    packages=['saves'],
    test_suite='tests',
    keywords="Persistence sqlite3 data",
    license="MIT"
    )
