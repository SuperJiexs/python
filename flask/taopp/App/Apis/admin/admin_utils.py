from flask import request, g
from flask_restful import abort
from .admin_users_utils import get_users
from App.utlis import MOVIE_USER,ADMIN_USER


from App.ext import cache


def _ty():


    token = request.args.get('token')

    if not token:
        abort(400, msg='没有登录')


    if not token.startswith(ADMIN_USER):
        abort(401,msg='token验证失败')


    user_id = cache.get(token)

    if not user_id:
        abort(400, msg='失效了')

    user = get_users(user_id)

    if not user:
        abort(400, msg='失效')

    g.user = user
    g.token = token


def login_required(func):

    def wrapper(*args,**kwargs):
        _ty()
        return func(*args,**kwargs)
    return wrapper


def check_permission(permission):
    def check_wrapper(func):
        def wrapper(*args,**kwargs):
            _ty()
            if not g.user.check_permission(permission):
                abort(403,msg='你没有vip 充值会是你快乐!')
            return func(*args,**kwargs)

        return wrapper
    return check_wrapper

