#!/usr/bin/env python

from setuptools import setup, find_packages

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Topic :: Internet',
    'Topic :: Database',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: OS Independent',
]

for ver in ['2', '2.4', '2.5', '2.6', '2.7']:
    CLASSIFIERS.append('Programming Language :: Python :: %s' % ver)

setup(
    name='permission-backend-nonrel',
    version='0.1',
    description='Django-nonrel authentication backend to support permissions and groups',
    packages=find_packages(exclude=('tests','tests.*')),
    author='Florian Hahn',
    author_email='flo@fhahn.com',
    url='https://github.com/fhahn/django-permission-backend-nonrel',
    platforms=['any'],
    include_package_data=True,
    classifiers=CLASSIFIERS
)
