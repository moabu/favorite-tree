"""
main.models.base
~~~~~~~~~~~~~~~~

this module contain base model class

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""

from main.extensions import db


class BaseModel(db.Model):
    """Base table class."""

    __abstract__ = True
    __table_args__ = {"extend_existing": True}

    """ Customize automatic string representation.
    """
    __repr_props__ = ()

    def __repr__(self):
        properties = [
            f"{prop}={getattr(self, prop)!r}"
            for prop in self.__repr_props__
            if hasattr(self, prop)
        ]
        return f"<{self.__class__.__name__} {' '.join(properties)}>"
