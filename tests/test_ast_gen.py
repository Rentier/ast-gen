from nose.tools import eq_, with_setup, nottest


"""
When some changes are made to the AST generating
source, one has to rebuild the AST under test. This
can be done with the command

python generate.py tests/fixtures/test_ast.cfg tests/ast_under_test.py

called from where generate.py resides.

It is assumed that it is created even before this
file is run, therefore, I can import the node classes
from the generated

ast_under_test.py

file and do my testing here.
"""
from tests.ast_under_test import *

identifier = Identifier('foo')
const = Constant('int', 40)
assignment = Assignment('+', identifier, const)
lst = Array(identifier, const)

def test_node_with_only_attributes():
    eq_(const.to_tuples(),
        ('Constant', 'int', 40))

def test_node_with_child_nodes():
    eq_(assignment.to_tuples(),
        ('Assignment', '+',
         ('Identifier', 'foo'),
         ('Constant', 'int', 40)))

def test_node_with_sequence_of_child_nodes():
    eq_(lst.to_tuples(),
        ('Array',
         [
             ('Identifier', 'foo'),
             ('Constant', 'int', 40)             
         ]))

    
    