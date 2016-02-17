# -*- coding: utf-8 -*-
# Author: Mark Spicer
# License: MIT

import os
from setuptools import setup
from setuptools import find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='openroast-api',
    version='0.1',
    description='',
    long_description=long_description,
    url='https://github.com/roastero/openroast-api',
    author='Mark Spicer',
    author_email='mds4680@rit.edu',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'falcon',
        'gunicorn',
        'redis',
        'requests',
        'apscheduler',
    ]
)
