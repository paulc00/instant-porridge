"""Sphinx configuration."""
project = "Instant Porridge"
author = "Paul Conway"
copyright = "2024, Paul Conway"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
