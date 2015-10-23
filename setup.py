#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from setuptools import setup

import caniuse


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()


setup(
    name='caniuse',
    version=caniuse.__version__,
    description='check whether a package name has been used on PyPI.',
    long_description=long_description,
    url='http://github.com/lord63/caniuse',
    author='lord63',
    author_email='lord63.j@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='PyPI package name used registered',
    packages=['caniuse'],
    install_requires=[
        'click>=4.0',
        'requests>=2.7.0'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'caniuse=caniuse.cli:cli']
    }
)
