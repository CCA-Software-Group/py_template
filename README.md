Template Python repository
--------------------------

[![Tests](https://github.com/CCA-Software-Group/py_template/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/CCA-Software-Group/py_template/actions/workflows/tests.yml)
[![Coverage](https://cca-software-group.github.io/py_template/coverage/badge.svg)](https://cca-software-group.github.io/py_template/coverage/index.html)
[![Docs](https://github.com/CCA-Software-Group/py_template/actions/workflows/docs.yml/badge.svg)](https://cca-software-group.github.io/py_template/)

This is a basic template for a Python repository, including:
- a source code directory `py_template`, with an example script `example_module.py` 
- a `test` folder for writing unit tests, with an example file
- a [documentation site](https://cca-software-group.github.io/py_template/index.html)
- continuous integration for tests, coverage, and docs (see `.github/workflows`).
- GitHub templates for users to submit issues

To make a new Python repo (or codespace) using this template:
1) Click on 'Use this template' button at the top-right of the GitHub page. 
2) In your new repo, rename (search and replace) all instances of 'py_template' with the name for your package. 
3) You can also update the `authors` field in `pyproject.toml` with your name(s) and email(s), and you can update `LICENSE.rst` as you like. (This template is partially based on the [OpenAstronomy packaging guide](https://github.com/OpenAstronomy/packaging-guide), so please retain that aspect of the license.)
5) Update the changelog in `HISTORY.rst` when you're ready to release your first version of the code!

After cloning your repo to your local machine, from the project's local root directory, you can:
- Install your package with all optional dependencies: 
`pip install -e ".[dev]"`
- Run your tests:
`pytest`
- Build your docs locally:
`tox -e build_docs` or `cd docs; make html`. After building the docs, view them with `open docs/_build/html/index.html`
