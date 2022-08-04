"""
main.extensions.routes_extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

this module contains an abstracted route extension

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""
from main.v1.tree.resource import blp as tree_routes


def register_routes(app):
    """Register blueprints"""
    app.register_blueprint(tree_routes, url_prefix="/")
