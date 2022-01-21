# cookiecutter-pylib-reqm

A `cookiecutter` template for Python library requirements management.

## Usage

To use this template, execute the following:

```shell
cookiecutter gh:jimustafa/cookiecutter-pylib-reqm
```

Accepting the default options will create a `requirements` directory in the current project directory.
The `requirements` directory will contain `dev.in`, a basic input file for `pip-tools`,
specifying that the dependencies of the library given in `setup.py` are required development dependencies.

## Explanation

For a Python library, the dependencies are typically specified in `setup.py`.
Development of a library generally requires a suite of tools, for tasks such as
writing documentation,
testing,
and version control.
While the dependencies of the library are given with rather loose version specifiers,
and usually assume semantic versioning,
the development tools constitute an environment that is likely best specified with "pinned" versions.

The [pip-tools](https://github.com/jazzband/pip-tools/) approach to requirements management is particularly simple and straightforward.
A selection of articles that give a detailed treatment of requirements management with `pip-tools` follows:

- https://jamescooke.info/a-successful-pip-tools-workflow-for-managing-python-package-requirements.html

During development, it is common for the library being developed to be installed in a virtual environment using the "editable mode" (`pip install --editable`).
With `pip-tools`, this can cause some issues associated with the transformation of relative paths

- https://github.com/jazzband/pip-tools/issues/204

so that

```shell
# requirements.in
--editable .
```

gets transformed to

```shell
# requirements.txt
--editable file:///path/to/pylib/
```

which have been addressed by

- https://github.com/jazzband/pip-tools/issues/398#issuecomment-311249142
- https://github.com/jamescooke/blog/issues/9

The approach taken here is to specify requirements for development tools in `dev.in`,
which is compiled to `dev.txt`.
The development requirements are constrained to be compatible with the dependencies of the library to ensure a consistent development environment.
