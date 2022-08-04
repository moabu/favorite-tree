"""
main.seeds.product
~~~~~~~~~~~~~~~

this module contain data seeder for product
note: this feature may be removed in the future

:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""
import uuid

from flask_seeder import Seeder
from sqlalchemy.exc import SQLAlchemyError

from main.models import Tree


class TreeSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    def run(self):
        items = [
            {
                "uid": uuid.uuid4(),
                "name": "Mohammad Abudayyeh",
                "favorite": "Olive Tree",
            }
        ]

        try:
            trees = []
            for item in items:
                slug = item["favorite"].replace(" ", "-").lower()
                tree = Tree.query.filter_by(slug=slug).first()
                if not tree:
                    trees.append(Tree(**item))

                self.db.session.add_all(trees)
                self.db.session.commit()
                print(f"Seeding trees completed")

        except SQLAlchemyError as e:
            self.db.session.rollback()
            print(e)

