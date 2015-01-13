#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup
from pip.download import PipSession

def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=PipSession(retries=3))
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="pytube",
    version="0.2.0",
    author="Nick Ficano",
    author_email="nficano@gmail.com",
    setup_requires=reqs,
    install_requires=reqs,
    packages=['pytube'],
    url="http://pytube.nickficano.com",
    license=open_file('LICENSE.txt').read(),
    scripts=['scripts/pytubectl'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video"
    ],
    description="A simple, yet versatile package for downloading "
                "YouTube videos.",
    long_description=open_file('README.rst').read(),
    zip_safe=True,
)
