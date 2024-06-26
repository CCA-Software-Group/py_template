Getting started
===============

| To make a new Python repo using `py_template`:
| 1) Click the 'Use this template' button at the top-right of the GitHub page. 
| 2) In your new repo, rename (search and replace) all instances of "py_template" with the name for your package. 
| 3) Update the `authors` field in `pyproject.toml`, `docs/conf.py` and `LICENSE.rst` (the template is partially based on the `OpenAstronomy packaging guide <https://github.com/OpenAstronomy/packaging-guide>`_, so please retain that aspect of the license).

| After cloning your repo to your computer, from the project's root directory, you can:
| 1) Install your package with all optional dependencies: 
| `pip install -e ".[dev]"`
| 2) Run your tests:
| `pytest .`
| 3) Run linting and formatting to see their effects:
| `black .` and `ruff check .`
| 4) Run type checking using mypy:
| `mypy --strict .`
| 5) Build your docs locally:
| `tox -e build_docs` or `cd docs; make html`. 
| After building the docs, view them with 
| `open docs/_build/html/index.html`

| When you're writing your software, you may want to:
| 1) Add new unit tests in `test/test_*.py` for new functions and classes. Test not just whether the new code runs, but also if it gives a sensible result.
| 2) Update the docs, including the main page (`docs/index.rst`), adding pages, and updating the API (`docs/py_API.rst`) when you add new functions and classes.
| 3) Optionally change the CI triggers for each of the actions in `.github/workflows`.
| 4) Update the changelog in `HISTORY.rst` when you're ready to release your first version of the code!