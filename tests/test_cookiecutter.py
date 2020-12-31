import contextlib
import os
try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

import cookiecutter
import piptools
import pytest
import sh


piptools_version = importlib_metadata.version('pip-tools')


@contextlib.contextmanager
def chdir(new_dir):
    old_dir = os.getcwd()
    try:
        os.chdir(new_dir)
        yield
    finally:
        os.chdir(old_dir)


@pytest.fixture
def context():
    return {
        'directory_name': 'requirements',
    }


OPTIONS = [
    {'preset': 'empty'},
    {'preset': 'basic'},
]


@pytest.mark.parametrize('extra_context', OPTIONS)
def test_bake(cookies, context, extra_context):
    result = cookies.bake(extra_context={**context, **extra_context})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'requirements'
    assert result.project.isdir()


@pytest.mark.parametrize('extra_context', OPTIONS)
def test_integration(pytestconfig, datadir, venv, extra_context):
    venv.install(f'pip-tools=={piptools_version}')

    with chdir(datadir):
        cookiecutter.main.cookiecutter(
            f'{pytestconfig.rootdir}',
            no_input=True,
            extra_context=extra_context,
        )
        with chdir('requirements'):
            sh.make(
                ['install-dev'],
                _env={
                    'LC_ALL': 'C.UTF-8',
                    'LANG': 'C.UTF-8',
                    'PATH': venv.bin
                }
            )

    venv.get_version('tqdm')

    if extra_context['preset'] == 'basic':
        venv.get_version('pytest')
        venv.get_version('sphinx')
        venv.get_version('tox')
