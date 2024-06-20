Template Python repository
--------------------------

This is a basic template for a Python repository, including:
| - a source code directory `py_template`, with an example script `example_module.py` 
| - a `test` folder for writing unit tests, with an example file
| - continuous integration 
| - documentation pages with ReadTheDocs
| - GitHub templates for users to submit issues

To make a new Python repo (or codespace) using this template:
| 1) Click on 'Use this template' button at the top-right of the GitHub page. 
| 2) In your new repo, rename (search and replace) all instances of 'py_template' with the name for your package. 
| 3) You can also update the `authors` field in `pyproject.toml` with your name(s) and email(s), and you can update `LICENSE.rst` as you like.
| 4) Update the changelog in `HISTORY.rst` when you're ready to release your first version of the code!

After cloning your repo to your local machine, from the project's local root directory, you can:
| - Install your package with all optional dependencies: 
| `pip install -e ".[all]"`
| - Run your tests (from the project's root directory):
| `pytest`
| - Build your docs:
| `tox -e build_docs`
