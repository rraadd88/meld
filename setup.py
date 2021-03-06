#!/usr/bin/env python

"""
========
setup.py
========

installs meld

USAGE :
python setup.py install

Or for local installation:

python setup.py install --prefix=/your/local/dir

"""

import sys
try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    from distutils.core import setup, find_packages, Extension
if (sys.version_info[0], sys.version_info[1],sys.version_info[2]) != (3, 6 ,5):
    raise RuntimeError('Python 3.6.5 required ')

# main setup
setup(
name='meld',
author='Rohan Dandage',
author_email='rraadd8888@gmail.com, rohan.dandage.1@ulaval.ca',
version='0.0.1',
url='https://github.com/rraadd88/meld',
download_url='https://github.com/rraadd88/meld/archive/master.zip',
# description='',
long_description='https://github.com/rraadd88/meld/README.md',
# keywords=['','',''],
license='General Public License v. 3',
install_requires=['biopython==1.71',
                  'regex==2018.7.11',
                    'pandas == 0.23.3',
                    # 'pyyaml',
                    'numpy==1.13.1',
                    'matplotlib==2.2.2',
                    'pysam==0.14.1',
                    'requests==2.19.1',
                    'scipy==1.1.0',
                    'tqdm==4.23.4',
                    'seaborn==0.8.1',
                    # 'pyensembl==1.4.0',
                    ],
platforms='Tested on Ubuntu 16.04 64bit',
packages=find_packages(),
package_data={'': ['meld/data']},
include_package_data=True,
entry_points={
    'console_scripts': ['meld = meld.pipeline:main',],
    },
)
