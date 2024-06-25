Template Python repository
--------------------------

[![Tests](https://github.com/CCA-Software-Group/py_template/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/CCA-Software-Group/py_template/actions/workflows/tests.yml)
[![Coverage](https://cca-software-group.github.io/py_template/coverage/badge.svg)](https://cca-software-group.github.io/py_template/coverage/index.html)
[![Docs](https://github.com/CCA-Software-Group/py_template/actions/workflows/docs.yml/badge.svg)](https://cca-software-group.github.io/py_template/)

This is a basic template for a Python repository, with the components needed to develop and release an open source software package. These include unit tests; type annotations; a documentation site with an API; and continuous integration for tests, code coverage, linting/formatting, type checking, and publishing the docs.

In more depth, the file structure is: 
- `.github` has two subfolders:
    * `ISSUE_TEMPLATE` has files that are templates users can select from when opening an issue in the repo on GitHub
    * `workflows` implements continuous integration (CI) through GitHub action files that are automatically run according to a chosen trigger. These are currently:
        1) `docs.yml` builds and deploys the [documentation site](https://cca-software-group.github.io/py_template/index.html) when a push is made to `main`.
        2) `format_lint.yml` lints and formats the code on each push using `ruff` and `black`.
        3) `tests.yml` runs tests with `pytest` on each push.
        4) `type_check.yml` runs type checking with `mypy` on each push. The CI continues even if the type checker finds errors.
- `docs` has the files used to build the documentation site with `Sphinx`, with the site content in `index.rst` and `py_API.rst`.
- `py_template` is the source code folder, with the necessary `__init__.py` and example code file, `example_module.py`.
- `test` has the unit tests, with example tests for the source code file in `test_example_module.py`. When you add new test files, they should start with `test_` so `pytest` recognizes them.
- `.gitignore` is a list of file types that are ignored when you push to the remote repo.
- `HISTORY.rst` is the change log that you should update as you implement the packaged version.
- `LICENSE.rst` has the package's license.
- `MANIFEST.in` has instructions for how to pre-process the package (which files to exclude) when preparing to release it to PyPI (the Python Package Index). Packages uploaded to PyPI can be installed by users with `pip`. 
- `README.md` is the file you're reading! It has badges that use the CI to display if the unit tests are passing, what percentage of the code is covered by the tests, and if the docs build and deploy is passing.
- `pyproject.toml` is the configuration file for the entire package. See the [Python docs](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) for a description of its contents.
- `tox.ini` is a configuration file used to set up testing. See the [tox docs](https://tox.wiki/en/latest/index.html) for a description of its contents.

To make a new Python repo (or codespace) using this template:
1) Click on 'Use this template' button at the top-right of the GitHub page. 
2) In your new repo, rename (search and replace) all instances of 'py_template' with the name for your package. 
3) You can also update the `authors` field in `pyproject.toml` with your name(s) and email(s), and the name and email fields in `LICENSE.rst` (the template is partially based on the [OpenAstronomy packaging guide](https://github.com/OpenAstronomy/packaging-guide), so please retain that aspect of the license).

After cloning your repo to your local machine, from the project's local root directory, you can:
- Install your package with all optional dependencies: 
`pip install -e ".[dev]"`
- Run your tests by simply entering:
`pytest`
- Build your docs locally:
`tox -e build_docs` or `cd docs; make html`. After building the docs, view them with `open docs/_build/html/index.html`
- Run linting and formatting to see their effects:
`black .` and `ruff check .`
- Run type checking using mypy:
`mypy --strict .`

When you're writing your software, you may want to:
1) Add new unit tests in `test/test_*.py` for new functions and classes. Test not just whether the new code runs, but also if it gives a sensible result.
2) Update the docs, including the main page (`docs/index.rst`), adding pages, and updating the API (`docs/py_API.rst`) when you add new functions and classes.
3) Optionally change the CI triggers for each of the actions in `workflows`.
4) Update the changelog in `HISTORY.rst` when you're ready to release your first version of the code!
