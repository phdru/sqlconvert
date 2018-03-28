#!/usr/bin/env python

from imp import load_source
from os.path import abspath, dirname, join
from setuptools import setup

versionpath = join(abspath(dirname(__file__)), 'sqlconvert', '__version__.py')
sqlconvert_version = load_source('sqlconvert_version', versionpath)

setup(name='sqlconvert',
      version=sqlconvert_version.__version__,
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
      scripts=['scripts/mysql2sql'],
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
      install_requires=[
          'sqlparse',
          'm_lib>=3.1',
          'm_lib.defenc>=1.0',
          'SQLObject>=2.2.1; python_version=="2.7"',
          'SQLObject>=3.0.0; python_version>="3.4"',
      ],
      )
