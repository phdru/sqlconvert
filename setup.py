#!/usr/bin/env python

from os.path import abspath, dirname, join
from setuptools import setup
import sys

versionpath = join(abspath(dirname(__file__)), 'sqlconvert', '__version__.py')
sqlconvert_version = {}

if sys.version_info[:2] == (2, 7):
    execfile(versionpath, sqlconvert_version)  # noqa: F821 'execfile' Py3

elif sys.version_info >= (3, 4):
    exec(open(versionpath, 'rU').read(), sqlconvert_version)

else:
    raise ImportError("sqlconvert requires Python 2.7 or 3.4+")

setup(
    name='sqlconvert',
    version=sqlconvert_version['__version__'],
    description='Broytman sqlconvert',
    long_description=open('README.rst', 'rU').read(),
    long_description_content_type="text/x-rst",
    author='Oleg Broytman',
    author_email='phd@phdru.name',
    url='https://phdru.name/Software/Python/sqlconvert/',
    project_urls={
        'Homepage': 'https://phdru.name/Software/Python/sqlconvert/',
        'Documentation':
            'https://phdru.name/Software/Python/sqlconvert/docs/',
        'Download': 'https://pypi.org/project/sqlconvert/%s/'
        % sqlconvert_version['__version__'],
        'Git repo': 'https://git.phdru.name/sqlconvert.git/',
        'Github repo': 'https://github.com/phdru/sqlconvert',
        'Issue tracker': 'https://github.com/phdru/sqlconvert/issues',
    },
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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=['sqlconvert'],
    scripts=['scripts/mysql2sql'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
        'SQLObject>=2.2.1; python_version=="2.7"',
        'SQLObject>=3.0.0; python_version>="3.4"',
        'm_lib.defenc>=1.0',
        'm_lib>=3.1',
        'sqlparse',
    ],
)
