from flask import session, request
from app.extends.error import HttpError


def check_login():
    if request.endpoint != 'admin.login' and 'department' not in session:
        raise HttpError(401, '请先登录')
