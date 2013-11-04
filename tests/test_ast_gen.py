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

identifier = Identifier('foo')
const = Constant('int', 40)
assignment = Assignment('+', identifier, const)


def test_creates_py_file():
    pass

def test_node_with_only_attributes():
    eq_(const.clazz, 'int')
    eq_(const.value, 40)

def test_node_with_child_nodes():
    
    eq_(assignment.op, '+')
    eq_(assignment.lvalue.name, 'foo')
    eq_(assignment.rvalue.clazz, 'int')
    eq_(assignment.rvalue.value, 40)

def test_node_with_sequence_of_child_nodes():
    lst = Array([identifier, const])
    eq_(len(lst.items), 2)
    eq_(lst.items[0].name, 'foo')
    eq_(lst.items[1].clazz, 'int')
    eq_(lst.items[1].value, 40)

    
    