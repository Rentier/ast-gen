import os, sys
from distutils.core import setup


setup(
    # metadata
    name='ast-gen',
    description='AST generator for Python',
    long_description="""
    Given a config file describing AST nodes
    and their respective attributes or children,
    it creates a file containing these node classes.
    """,
    license='BSD',
    version='0.1',
    author='Eli Bendersky, Jan-Christoph Klie',
    maintainer='Jan-Christoph Klie ',
    author_email='git@mrklie.com',
    url='https://github.com/rentier/ast-gen',
    platforms='Cross Platform',
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',],
    packages=['astgen'],
    package_data={},
)


