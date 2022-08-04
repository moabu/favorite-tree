"""
core
~~~~

This module contains pre-configured instances (app, worker, etc.) for CLI.

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""

from main.app import create_app

# By instantiating the Flask app, we can import this object into other entrypoints.
#
# Example:
#
#     # Flask builtin dev server
#     FLASK_APP=main.core:app FLASK_ENV=development poetry run flask run
#
#     # Gunicorn server
#     FLASK_ENV=production poetry run gunicorn main.core:app -b ":5000"
#
app = create_app()
