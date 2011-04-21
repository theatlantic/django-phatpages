import os
from setuptools import setup, find_packages

from staticpages import VERSION


f = open(os.path.join(os.path.dirname(__file__), 'README.txt'))
readme = f.read()
f.close()

setup(
    name='django-fatpages',
    version=".".join(map(str, VERSION)),
    description='django-fatpages is a reusable Django application for simple static pages.',
    long_description=readme,
    author='Josh West',
    author_email='',
    url='https://github.com/theatlantic/django-fatpages',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)


