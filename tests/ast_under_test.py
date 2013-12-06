#-----------------------------------------------------------------
# ** ATTENTION **
# This code was automatically generated from the file:
# tests/fixtures/test_ast.cfg
#
# Do not modify it directly. Modify the configuration file and
# run the generator again.
# ** ** *** ** **
#
# AST Node classes.
#
# Copyright (C) 2008-2013, Eli Bendersky
#               2013,      Jan-Christoph Klie 
# License: BSD
#-----------------------------------------------------------------


import sys


class Node(object):
    """ Abstract base class for AST nodes.
    """
    def children(self):
        """ A sequence of all children that are Nodes
        """
        pass

    def __str__(self):
        return self.show()

    def __repr__(self):
        return str(self.to_tuples())

    def to_tuples(self):
        result = [self.__class__.__name__]

        if self.attr_names:
            vlist = [getattr(self, n) for n in self.attr_names]
            attrlst = [v for v in vlist]
            result.extend(attrlst)

        for (child_name, child) in self.children():
            result.append( child.to_tuples() )
        return tuple(result)

    def show(self,
             buf=None,
             offset=0,
             attrnames=False,
             nodenames=False,
             showcoord=False,
             _my_node_name=None):
        """ Pretty print the Node and all its attributes and
            children (recursively) to a buffer.

            buf:
                Open IO buffer into which the Node is printed.
                If it is None or let empty, instead a string
                is returned

            offset:
                Initial offset (amount of leading spaces)

            attrnames:
                True if you want to see the attribute names in
                name=value pairs. False to only see the values.

            nodenames:
                True if you want to see the actual node names
                within their parents.

            showcoord:
                Do you want the coordinates of each Node to be
                displayed.
        """
        s = ''
        lead = ' ' * offset
        if nodenames and _my_node_name is not None:
            s += lead + self.__class__.__name__+ ' <' + _my_node_name + '>: '
        else:
            s += lead + self.__class__.__name__+ ': '

        if self.attr_names:
            if attrnames:
                nvlist = [(n, getattr(self,n)) for n in self.attr_names]
                attrstr = ', '.join('%s=%s' % nv for nv in nvlist)
            else:
                vlist = [getattr(self, n) for n in self.attr_names]
                attrstr = ', '.join('%s' % v for v in vlist)
            s += attrstr

        if showcoord: s += ' (at %s)' % self.coord
        s += '\n'

        for (child_name, child) in self.children():
            s += child.show(
                buf,
                offset=offset + 2,
                attrnames=attrnames,
                nodenames=nodenames,
                showcoord=showcoord,
                _my_node_name=child_name)

        if buf is None: return s
        else: buf.write(s)

class NodeVisitor(object):
    """ A base NodeVisitor class for visiting c_ast nodes.
        Subclass it and define your own visit_XXX methods, where
        XXX is the class name you want to visit with these
        methods.

        For example:

        class ConstantVisitor(NodeVisitor):
            def __init__(self):
                self.values = []

            def visit_Constant(self, node):
                self.values.append(node.value)

        Creates a list of values of all the constant nodes
        encountered below the given node. To use it:

        cv = ConstantVisitor()
        cv.visit(node)

        Notes:

        *   generic_visit() will be called for AST nodes for which
            no visit_XXX method was defined.
        *   The children of nodes for which a visit_XXX was
            defined will not be visited - if you need this, call
            generic_visit() on the node.
            You can use:
                NodeVisitor.generic_visit(self, node)
        *   Modeled after Python's own AST visiting facilities
            (the ast module of Python 3.0)
    """
    def visit(self, node):
        """ Visit a node.
        """
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """ Called if no explicit visitor function exists for a
            node. Implements preorder visiting of the node.
        """
        for c_name, c in node.children():
            self.visit(c)


class Assignment(Node):
    def __init__(self, op, lvalue, rvalue, coord=None):
        self.op = op
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.coord = coord

    def children(self):
        nodelist = []
        if self.lvalue is not None: nodelist.append(("lvalue", self.lvalue))
        if self.rvalue is not None: nodelist.append(("rvalue", self.rvalue))
        return tuple(nodelist)

    attr_names = ('op',)

class Constant(Node):
    def __init__(self, clazz, value, coord=None):
        self.clazz = clazz
        self.value = value
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('clazz','value',)

class Identifier(Node):
    def __init__(self, name, coord=None):
        self.name = name
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('name',)

class Array(Node):
    def __init__(self, items, coord=None):
        self.items = items
        self.coord = coord

    def children(self):
        nodelist = []
        for child in self.items or []:
            nodelist.append(child)
        return tuple(nodelist)

    attr_names = ()

