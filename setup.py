#!/usr/bin/env python

from imp import load_source
from os.path import abspath, dirname, join

try:
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    pass
try:
    from setuptools import setup
    is_setuptools = True
except ImportError:
    from distutils.core import setup
    is_setuptools = False

versionpath = join(abspath(dirname(__file__)), 'mysql2sql', '__version__.py')
load_source('mysql2sql_version', versionpath)
from mysql2sql_version import __version__  # noqa

setup(name='mysql2sql',
      version=__version__,
      description='Broytman mysql2sql',
      long_description=open('README.txt', 'rtU').read(),
      author='Oleg Broytman',
      author_email='phd@phdru.name',
      url='http://phdru.name/Software/Python/',
      license='GPL',
      platforms=['any'],
      keywords=[''],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 2 :: Only',
      ],
      packages=['mysql2sql'],
      package_data={'mysql2sql': []},
      scripts=[],
      requires=[],
      )
