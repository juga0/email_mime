#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab
# Copyright 2017 juga (juga at riseup dot net), MIT license.

"""Setup."""
from setuptools import find_packages, setup


setup(
    name='emailpgp',
    version='0.0.1',
    description='TBD',
    long_description='TBD',
    author='juga',
    author_email='juga@riseup.net',
    license='MIT',
    url='https://github.com/juga0/emailpgp',
    packages=['mime'],
    extras_require={
        'dev': ['ipython', 'pyflakes', 'pep8'],
    },
    zip_safe=False,
    include_package_data=True,
    keywords='python mime OpenPGP',
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Environment :: Console",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Networking',
    ],
)