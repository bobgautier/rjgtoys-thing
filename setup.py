#!/usr/bin/python3

try:
    from rjgtoys.projects import setup
except ImportError:
    from setuptools import setup

setup(
    name = "rjgtoys-thing",
    version = "0.0.3",
    author = "Robert J. Gautier",
    author_email = "bob.gautier@gmail.com",
    url = "https://github.com/bobgautier/rjgtoys-Thing",
    description = ("A Python dict that behaves a bit like a JavaScript object"),
    namespace_packages=['rjgtoys'],
    packages = ['rjgtoys','rjgtoys.thing'],
    install_requires = [
    ],
    extras_require = {
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
