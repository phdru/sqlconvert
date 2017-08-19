#!/usr/bin/env python

import sys
from imp import load_source
from os.path import abspath, dirname, join

try:
    from setuptools import setup
    is_setuptools = True
except ImportError:
    from distutils.core import setup
    is_setuptools = False

versionpath = join(abspath(dirname(__file__)), 'sqlconvert', '__version__.py')
load_source('sqlconvert_version', versionpath)
# Ignore: E402 module level import not at top of file
from sqlconvert_version import __version__  # noqa

kw = {}
if is_setuptools:
    if (sys.version_info[:2] == (2, 7)):
        PY2 = True
    elif (sys.version_info[0] == 3) and (sys.version_info[:2] >= (3, 4)):
        PY2 = False
    else:
        raise ImportError("sqlconvert requires Python 2.7 or 3.4+")

    kw['install_requires'] = [
        'sqlparse',
        'm_lib.defenc>=1.0', 'm_lib>=3.1',
    ]
    if PY2:
        kw['install_requires'].append('SQLObject>=2.2.1')
    else:
        kw['install_requires'].append('SQLObject>=3.0.0')

setup(name='sqlconvert',
      version=__version__,
      description='Broytman sqlconvert',
      long_description=open('README.rst', 'rU').read(),
      author='Oleg Broytman',
      author_email='phd@phdru.name',
      url='http://phdru.name/Software/Python/sqlconvert/',
      license='GPL',
      keywords=['sql', 'mysql', 'postgresql', 'sqlite', 'insert'],
      platforms='Any',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      packages=['sqlconvert'],
      package_data={},
      scripts=['scripts/mysql2sql'],
      **kw
      )
