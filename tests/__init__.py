from astgen.ast_gen import ASTCodeGenerator

import os, sys, importlib

TEST_AST_CFG = os.path.join('fixtures', 'test_ast.cfg')
TEST_AST_MODULE = 'test_ast'
TEST_AST_PY = TEST_AST_MODULE + '.py'

def setup():
    """ Generates the node classes as described in the
    TEST_AST_CFG file, and saves it under the name of
    TEST_AST_MODULE.
    """
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    ast_gen = ASTCodeGenerator(TEST_AST_CFG)
    ast_gen.generate(open(TEST_AST_PY, 'w'))

def teardown():
    """ Cleans up after the code generation: If existing,
    removes the generated python file and its binary.
    """
    try:        
        os.remove(TEST_AST_PY)
        os.remove(TEST_AST_PY + 'c')
    except OSError as e:
        pass
