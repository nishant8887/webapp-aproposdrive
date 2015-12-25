#!/usr/bin/env python

import os
from setuptools import setup

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

setup(
    name='Aproposdrive',
    version='1.0',
    description='Website',
    author='Nishant Shelar',
    author_email='nishant8887@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=open('%saproposdrive/requirements.txt' % os.environ.get('OPENSHIFT_REPO_DIR', PROJECT_ROOT)).readlines(),
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
