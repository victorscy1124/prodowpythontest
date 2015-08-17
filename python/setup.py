# -*- coding: utf-8 -*-
from setuptools import setup

requirements = [
    'bottle',
    'pymysql',
    'requests',
    'mako'
]

setup(
    name = "prodowpythontest",
    version = "0.1.0",
    author="Victor Liu",
    author_email='victorscy1124@gmail.com',
    description="prodow",
    license = "BSD",
    keywords = "fundpromo",
    url='https://github.com/victorscy1124/prodowpythontest',
    packages=['controller', 'model', 'view'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=requirements,
)