"""
main.v1.tree.resource
~~~~~~~~~~~~~~~~~~~~~

this module contain resource classes for tree module

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""

from faker import Faker
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError

from main.extensions import BlueprintApi, db
from main.v1.tree.schema import TreeSchema, UpdateTreeSchema
from main.models.tree import Tree

blp = BlueprintApi("Tree", __name__)
fake = Faker()


@blp.route("/tree")
class FavoriteTree(MethodView):
    """
    tree
    get : fetch favorite tree
    #TODO patch: update favorite tree
    """

    @blp.etag
    @blp.response(
        200,
        TreeSchema(many=False),
        example=dict(
            uid="127327384893",
            name="Jane Doe",
            favorite="Yellow Birch"
        ))
    def get(self):
        """
        get favorite tree
        :return: tree object : JSON
        """
        return Tree.query.first_or_404()

    @blp.etag
    @blp.arguments(
        UpdateTreeSchema,
        example=dict(
            name=fake.name(),
        ),
    )
    @blp.response(201)
    def patch(self, data):
        """
        update favorite tree
        :param data: TreeSchema
        :return:
        """
        item = Tree.query.first_or_404()
        blp.check_etag(item, TreeSchema)

        item.favorite = data["favorite"]

        try:
            db.session.add(item)
            db.session.commit()
            message = "Favorite tree successfully updated."
            return {"status": "success", "message": message}
        except SQLAlchemyError as error:
            db.session.rollback()
            message = [str(x) for x in error.args]
            abort(400, message=error.__class__.__name__, errors=message)


