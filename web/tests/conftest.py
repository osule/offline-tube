import pytest

from web.manage import app as flask_app


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    settings_override = {
        'TESTING': True,
    }

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return flask_app

@pytest.fixture(scope='session')
def client(app):
    test_client = app.test_client()
    return test_client