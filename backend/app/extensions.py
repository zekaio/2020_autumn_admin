"""
扩展
"""
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Query, Session

cors = CORS(supports_credentials=True)


class _SQLAlchemy(SQLAlchemy):
    session: Session


db = _SQLAlchemy()


class Model(db.Model):
    __abstract__ = True

    query: Query

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
