"""
main.models.tree
~~~~~~~~~~~~~~~~~~~~~~~~

this module contain model classes for the tree module

:copyright: (c) 2022 by Mohammad.
:license: All Rights Reserved, see LICENSE for more details.
"""
from dataclasses import dataclass

from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property

from main.extensions import db
from main.models.base import BaseModel

@dataclass
class Tree(BaseModel):
    """
    Tree model.
    :relationships:
    - undefined
    """
    __tablename__ = "tree"

    # columns
    uid = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    favorite = db.Column(db.String(255), unique=True, nullable=False)

    @hybrid_property
    def slug(self):
        return self.favorite.replace(" ", "-").lower()

    @slug.expression
    def slug(self):
        return func.lower(func.replace(self.favorite, " ", "-"))
