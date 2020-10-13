from flask import session

from app.models.database import *


def get_users():
    return [user.to_dict() for user in (
        User
            .query
            .filter(User.first.like(f"{session.get('department')}%"))
            .order_by(User.id.desc())
            .all()
    )]


def update_users(first_id: int):
    return [user.to_dict() for user in (
        User
            .query
            .filter(User.first.like(f"{session.get('department')}%"))
            .filter(User.id > first_id)
            .order_by(User.id.desc())
            .all()
    )]


def get_all_users():
    return [user.to_list()[1:] for user in (
        User
            .query
            .filter(User.first.like(f"{session.get('department')}%"))
            .all()
    )]


def count():
    return User.query.filter(User.first.like(f"{session.get('department')}%")).count()
