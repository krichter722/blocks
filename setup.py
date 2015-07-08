#!/usr/bin/env python3.3

from setuptools import setup
import sys

app_name = 'blocks'

if sys.version_info < (3,):
    raise Exception("%s's setup.py needs to be run with python3" % (app_name,))

setup(
    name=app_name,
    version='0.1.4',
    author='Gabriel de Perthuis',
    author_email='g2p.code+blocks@gmail.com',
    url='https://github.com/g2p/blocks',
    license='GNU GPL',
    keywords='bcache lvm storage partitioning ssd',
    description='Conversion tools for block devices',
    entry_points={
        'console_scripts': [
            'blocks = blocks.__main__:script_main']},
    packages=[
        'blocks',
    ],
    include_package_data=True,
    # See requirements.txt for installable versions
    install_requires=[
        'maintboot',
        'python-augeas >= 0.4.2a0',
        'pyparted > 3.10a0'],
    classifiers='''
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.3
        License :: OSI Approved :: GNU General Public License (GPL)
        Operating System :: POSIX :: Linux
        Intended Audience :: System Administrators
        Intended Audience :: End Users/Desktop
        Topic :: System :: Filesystems
        Topic :: Utilities
        Environment :: Console
    '''.strip().splitlines(),
    long_description='''
    Conversion tools for block devices.

    Convert between raw partitions, logical volumes, and bcache
    devices witout moving data.

    See `github.com/g2p/blocks <https://github.com/g2p/blocks#readme>`_
    for installation and usage instructions.''')

