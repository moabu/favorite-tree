"""
main.app
~~~~~~~~

This module consists of various helpers related to Flask's app.

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""
import sys
import logging
from flask import Flask

from main.config import ConfigLoader
from main.config import get_instance_path
from main.extensions import (
    api, cors, db,
    migrate, toolbar,
    seeder, cache
)
from main.extensions.routes_extension import register_routes


def create_app():
    """Factory function to create Flask app.

    :return: :class:`flask.Flask` object
    """
    # app with instance path set to home directory
    app = Flask(
        __name__,
        instance_path=get_instance_path(),
        instance_relative_config=True,
        subdomain_matching=True,
    )

    # load default configuration
    app.config.from_object(ConfigLoader.set_config(sys.argv))

    # load extensions
    db.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)
    cors.init_app(app, resources=r"/*")
    api.init_app(app)
    seeder.init_app(app, db)
    cache.init_app(app)

    # register blueprint
    register_routes(api)

    requested_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = requested_logger.handlers[:]
    logging.getLogger('engineio').setLevel(logging.ERROR)
    # return Flask app
    return app


