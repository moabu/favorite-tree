"""
test_app
~~~~~~~~

This module consists of testcases for :module:`main.app` module.

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""
from unittest.mock import patch

import pytest


@pytest.mark.parametrize(
    "env, argv",
    [
        ("", ""),
        ("testing", ""),
        ("", ["env", "testing"]),
        ("", ["env"]),
    ],
)
def test_create_app(monkeypatch, env, argv):
    """Test factory function that creates Flask's app."""
    from main.app import create_app

    monkeypatch.setenv("FLASK_ENV", env)
    monkeypatch.setattr("sys.argv", argv)

    if not env:
        # Default if env is empty to testing
        env = "testing"

    app = create_app()
    assert app.config["ENV"] == env
    # Flask app has ``app_context`` attr
    assert hasattr(app, "app_context")
