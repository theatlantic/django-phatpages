#!/usr/bin/python

# Use setuptools if we can
try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-phatpages',
    version='0.2.1',
    description='A reusable Django application for simple static pages.',
    long_description=open('README.txt').read(),
    author='Josh West',
    url='https://github.com/theatlantic/django-phatpages',
    download_url='https://github.com/theatlantic/django-phatpages/tarball/master',
    packages=['phatpages'],
)
