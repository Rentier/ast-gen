===============
ast-gen 
===============

This is a small module to generate AST node classes automatically for Python. It originated in the `pyparser git`_ project. It was forked and then extracted from thre to wrap it into a self-contained module and to enhance it with additional features.

Installation
------------

Installing ast-gen is very simple. Once you download and unzip the package, you just have to execute the standard ::

	python setup.py install 

The setup script will then place the ast-gen module into site-packages in your Python's installation library. To install it via **pip**, just use::

	pip install -e "git+https://github.com/Rentier/ast-gen.git#egg=astgen" 

Usage
-----

The idea behind this module is to describe the nodes, their attributes and children in a config file. From it, a python file containing one class for every node is generated and then can be used without any dependency to this project.

Config
^^^^^^

Each entry is a Node sub-class name, listing the attributes and child nodes of the class: ::

	<name>*     - a child node
	<name>**    - a sequence of child nodes
	<name>      - an attribute.

Example: ::

	BinaryOp: [op, left*, right*]
	Constant: [type, value]
	ExprList: [exprs**]

Code Generation
^^^^^^^^^^^^^^^

To generate the file containing the described nodes, just run::

	from astgen.ast_gen import ASTCodeGenerator
	ast_gen = ASTCodeGenerator(**PATH_TO_CONFIG.cfg**)
	ast_gen.generate(open(**PATH_TO_WHERE_TO_SAVE**, 'w'))

Build status
------------

.. image:: https://travis-ci.org/Rentier/ast-gen.png?branch=master   :target: https://travis-ci.org/Rentier/ast-gen

.. _pyparser git: https://github.com/eliben/pycparser
