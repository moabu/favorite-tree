"""
conftest
~~~~~~~~

This module shares pytest fixtures commonly-used in testcases.

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""
import os

import pytest

current_path = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('FLASK_ENV', 'testing')
    monkeypatch.setenv('SQLALCHEMY_DATABASE_URI_FILEPATH', os.path.join(current_path, "sql_secrets", "sql_uri.txt"))


@pytest.fixture(scope="session")
def app():
    """This function creates Flask app instance for testing.
    The returned object is a pytest fixture that can be used
    throughout the testcases.

    Example:

        def test_views_login(app):
            with app.test_client() as client:
                rv = client.get("/login")
                assert rv.status_code == 200
    """
    import os
    from main.app import create_app

    os.environ["FLASK_ENV"] = "testing"

    app = create_app()

    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()
