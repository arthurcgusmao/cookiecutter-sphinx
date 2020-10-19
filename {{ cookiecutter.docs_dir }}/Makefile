# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the ones defined with ?=
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

SPHINXAPIDOC   ?= sphinx-apidoc
MODULEPATH     = ../{{ cookiecutter.module_dir }}
EXCLUDEPATTERN =
DOCSTRINGOPTS  = --force --separate --module-first


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Automatically generate docs from our module's docstrings
# See https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
apidoc:
	@$(SPHINXAPIDOC) $(DOCSTRINGOPTS) \
		-o "$(SOURCEDIR)" "$(MODULEPATH)" "$(EXCLUDEPATTERN)"

# Generic command for doing everything
rebuild:
	make clean
	make apidoc
	make html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
