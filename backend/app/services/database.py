from flask import session
import typing

from app.models.database import *


def get_users(last_id: int, limit: int):
    department = session.get('department')

    query = User.query.filter_by(first=department)

    if last_id:
        query = query.filter(User.id < last_id)

    users: typing.List[User] = (
        query
            .order_by(User.id.desc())
            .limit(limit)
            .all()
    )

    return [user.to_dict() for user in users]


def update_users(first_id: int):
    department = session.get('department')

    users: typing.List[User] = (
        User
            .query
            .filter_by(first=department)
            .filter(User.id > first_id)
            .all()
    )

    return [user.to_dict() for user in users]


def get_all_users():
    department = session.get('department')

    users: typing.List[User] = (
        User
            .query
            .filter_by(first=department)
            .all()
    )

    return [user.to_list()[1:] for user in users]
