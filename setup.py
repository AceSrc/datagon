#!/usr/bin/env python
from setuptools import Command, setup, find_packages

setup(
    name = 'datagon',
    version = '0.1',
    license = 'MIT',
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'datagon = datagon.cli:main',   
        ],
    }
)
