# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('.'))

project = 'GIST3- Módulo Planeamento'
copyright = '2024, Bruno Oliveira'
author = 'Bruno Oliveira'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',  # Add 'sphinx.ext.mathjax' if you need math support
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',     # serve para ter as referencias como utilizamos no latex. P
                                # ara o usar é necessario instalar o package: pip install sphinxcontrib-bibtex
    'sphinxcontrib.plantuml',   #serve para fazer parse de ficheiros plantUML
                                # ara o usar é necessario instalar o package: pip install sphinxcontrib-plantuml
    # 'myst_parser',          # For Markdown support requires to be installed
]

bibtex_bibfiles = ['references.bib']

templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme used for HTML. For a list of sphinx themes visit https://sphinx-themes.org/
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

# LaTeX options for PDF
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

# If you want custom LaTeX preamble, you can add it here
latex_documents = [
    ('index', 'MyBook.tex', 'My Book Title', 'Your Name', 'manual'),
]

# The name of the image file (relative to this directory) to place at the top
# html_logo = 'logo.png'

# The name of the image file (within the static path) to use as favicon of the docs. This file should be a windows icon
# file (.ico) being 16x16 or 32x32
