from flask import g
from flask_restful import Resource,reqparse,abort
from .movie_user_utils import get_users
from App.ext import cache
from .movie_order_utils import login_required,check_permission
from ...model.movie_user.MovieUser import VIP_USER,COMMOM_USER


class MovieOrdersApis(Resource):
    @login_required
    def post(self):
        user=g.user

        return {'msg':'post order111 ok'}

class MovieOrderApis(Resource):

    @check_permission(VIP_USER)
    def put(self,order_id):

        return {'msg':'修改成功'}



