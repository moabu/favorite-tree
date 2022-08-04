"""
v1.tree.schema
~~~~~~~~~~~~~~

this module contain schema classes for the tree module

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""

import marshmallow as ma
from marshmallow import EXCLUDE


class TreeSchema(ma.Schema):
    """
    Tree Schema
    """

    class Meta:
        unknown = EXCLUDE
        ordered = True
    name = ma.fields.Str(required=True)
    favorite = ma.fields.Str(required=True)
    slug = ma.fields.Str(dump_only=True)


class UpdateTreeSchema(TreeSchema):
    """
    Update tree schema.
    """

    class Meta:
        fields = ("favorite",)
