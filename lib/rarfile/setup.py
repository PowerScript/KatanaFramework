#! /usr/bin/env python

from distutils.core import setup

import rarfile

ver = rarfile.__version__
ldesc = open("README.rst").read().strip()
sdesc = ldesc.split('\n')[0].split(' - ')[1].strip()

setup(
    name = "rarfile",
    version = ver,
    description = sdesc,
    long_description = ldesc,
    author = "Marko Kreen",
    license = "ISC",
    author_email = "markokr@gmail.com",
    url = "https://github.com/markokr/rarfile",
    py_modules = ['rarfile'],
    keywords = ['rar', 'unrar', 'archive'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Compression",
    ]
)

