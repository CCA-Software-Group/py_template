Template Python repository
--------------------------

[![Tests](https://github.com/CCA-Software-Group/py_template/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/CCA-Software-Group/py_template/actions/workflows/tests.yml)
[![Coverage](https://cca-software-group.github.io/py_template/coverage/badge.svg)](https://cca-software-group.github.io/py_template/coverage/index.html)
[![Docs](https://github.com/CCA-Software-Group/py_template/actions/workflows/docs.yml/badge.svg)](https://cca-software-group.github.io/py_template/)

This is a basic template for a Python repository, with the components needed to develop and release an open source software package. These include unit tests; type annotations; a documentation site with an API; and continuous integration for tests, code coverage, linting/formatting, type checking, and publishing the docs.

See the [docs](https://cca-software-group.github.io/py_template/) for a 'Getting Started' guide with steps on how to make your own Python repo using this template and what to do next to build your own package. 

The file structure of this repo is: 
1) `.github` has two subfolders:
    * `ISSUE_TEMPLATE` has files that are templates users can select from when opening an issue in the repo on GitHub
    * `workflows` implements continuous integration (CI) through GitHub 'actions' that are automatically run according to a chosen trigger. These are currently:
        - `docs.yml` builds and deploys the [documentation site](https://cca-software-group.github.io/py_template/index.html) when a push is made to `main`.
        - `format_lint.yml` lints and formats the code on each push using `ruff` and `black`.
        - `tests.yml` runs tests with `pytest` on each push.
        - `type_check.yml` runs type checking with `mypy` on each push. The CI continues even if the type checker finds errors.
2) `docs` has the files used to build the documentation site with `Sphinx`, with the site content in `index.rst` and `py_API.rst`.
3) `py_template` is the source code folder, with the necessary `__init__.py` and example code file, `example_module.py`.
4) `test` has the unit tests, with example tests for the source code file in `test_example_module.py`. When you add new test files, they should start with `test_` so `pytest` recognizes them.
5) `.gitignore` is a list of file types that are ignored when you push to the remote repo.
6) `HISTORY.rst` is the change log that you should update as you implement the packaged version.
7) `LICENSE.rst` has the package's license.
8) `MANIFEST.in` has instructions for how to pre-process the package (which files to exclude) when preparing to release it to PyPI (the Python Package Index). Packages uploaded to PyPI can be installed by users with `pip`. 
9) `README.md` is the file you're reading! It has badges that use the CI to display if the unit tests are passing, what percentage of the code is covered by the tests, and if the docs build and deploy is passing.
10) `pyproject.toml` is the configuration file for the entire package. See the [Python docs](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) for a description of its contents.
11) `tox.ini` is a configuration file used to set up testing. See the [tox docs](https://tox.wiki/en/latest/index.html) for a description of its contents.
