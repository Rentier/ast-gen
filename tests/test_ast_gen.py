from nose.tools import eq_, with_setup, nottest

from test_ast import *

"""
This test file does many hidden things, mostly in
a setup function in the nearby __init__.py file.

There, I create on the fly a AST class with ast_gen
from a fixture config file, found in

fixtures/test_ast.cfg

This is created even before this file is run,
therefore, I can import the node classes from the
generated

test_ast.py

file and do my testing here.
"""

def test_creates_py_file():
    pass

def test_node_with_only_attributes():
    const = Constant('int', 42)
    eq_(const.clazz, 'int')
    eq_(const.value, 42)
