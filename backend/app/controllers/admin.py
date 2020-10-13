from flask import Blueprint, session, request
import flask_excel as excel
import typing

from app.config.config import BaseConfig
from app.extends.error import HttpError
from app.extends.result import Result
from app.models.controller import UserModel
from app.services import database

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# 登录
@admin_bp.route('/session', methods=['post'])
def login():
    user: UserModel = UserModel.get_parameters()
    if user.password == BaseConfig.admin_password and user.username in BaseConfig.departments:
        session['department'] = user.username
    else:
        raise HttpError(400, '用户名或密码错误')
    return Result.OK().msg('登录成功').build()


@admin_bp.route('/user/detail')
def get_detail():
    last_id = request.args.get('last_id') or 0
    limit = request.args.get('limit') or 10

    return Result.OK().data(database.get_users(last_id, limit)).build()


@admin_bp.route('/user/detail/update')
def update_detail():
    first_id = request.args.get('first_id')

    return Result.OK().data(database.update_users(first_id)).build()


@admin_bp.route('/user/excel')
def get_excel():
    title = ['姓名', '手机号', '性别', '年级', '校区', '学院', '宿舍', '第一志愿', '第二志愿', '服从调剂', '自我介绍']
    users: typing.List[list] = database.get_all_users()

    return excel.make_response_from_array([title, *users], file_type='xlsx',
                                          file_name=u'{}'.format(session.get('department')))
