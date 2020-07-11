import uuid

from flask_restful import Resource,reqparse,abort
from ..ext import cache

parse_base=reqparse.RequestParser()
parse_base.add_argument('name',type=str,required=True,help='请输入用户名')
parse_base.add_argument('password',type=str,required=True,help='请输入密码')



class denglu(Resource):

    def post(self):

        args=parse_base.parse_args()

        user=args.get('name')
        password=args.get('password')

        if  user == 'zhangjie' and password == '123456':

        #   token=uuid.uuid4().hex
        #   cache.set(token,user,timeout=60*60*24*7)

            data={
                'msg': '登录成功',
                'status': 200,
            }
            return data
        else:
            abort(400, msg='用户名或密码错误')