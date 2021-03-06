# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

REQUIREMENTS = [
    'grpcio',
    'google-api-core'
]


CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.7',
    'Topic :: Communications',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]

setup(
    name='chirpstack-api',
    version = "3.3.2",
    url='https://github.com/iBrick/chirpstack-api',
    author='InnoLabs',
    author_email='mail@lo-ra.net',
    license='',
    description='Python API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
)
