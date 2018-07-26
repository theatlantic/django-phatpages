#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='django-phatpages',
    version='3.0.0',
    description='A reusable Django application for simple static pages.',
    long_description=open('README.txt').read(),
    author='Josh West',
    url='https://github.com/theatlantic/django-phatpages',
    download_url='https://github.com/theatlantic/django-phatpages/tarball/master',
    packages=find_packages(),
)
