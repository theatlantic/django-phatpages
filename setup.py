#!/usr/bin/python

# Use setuptools if we can
try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.txt'))
readme = f.read()
f.close()

setup(
    name='django-fatpages',
    version='0.1',
    description='A reusable Django application for simple static pages.',
    long_description=readme,
    author='Josh West',
    url='https://github.com/theatlantic/django-fatpages',
    download_url='https://github.com/theatlantic/django-fatpages/tarball/master',
    packages=['staticpages'],
)