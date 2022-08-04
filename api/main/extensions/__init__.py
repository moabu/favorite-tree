"""
main.extensions
~~~~~~~~~~~~~~~~

This module consists of Flask extensions.

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""

import os
from pathlib import Path

from flask_caching import Cache
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api, Blueprint
from flask_seeder import FlaskSeeder


# SQLAlchemy extension
db = SQLAlchemy()

# Migrate extension
migration_dir = os.path.join(str(Path(__file__).parent.parent), "migrations")
migrate = Migrate(directory=migration_dir)

# Flask CORS
cors = CORS()

# Debug toolbar extension (enabled in DEBUG mode only)
toolbar = DebugToolbarExtension()

# Flask Smorest
api = Api()

# Flask Seeder
seeder = FlaskSeeder()

# Flask Caching
cache = Cache()


class BlueprintApi(Blueprint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _prepare_response_content(data):
        if data is not None:
            return {"data": data}
        return None