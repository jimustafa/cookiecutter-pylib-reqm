import pytest


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
def test_bake_project(cookies, context, extra_context):
    result = cookies.bake(extra_context={**context, **extra_context})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'requirements'
    assert result.project.isdir()
