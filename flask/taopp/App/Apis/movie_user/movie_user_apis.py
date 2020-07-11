import uuid
from flask_restful import Resource,reqparse,abort,marshal,fields
from App.model.movie_user.MovieUser import MovieUser
from App.Apis.apis_contants import HTTP_OK,HTTP_CREATE_OK,USER_ACTION_LOGIN,USER_ACTION_REGISTER
from .movie_user_utils import get_users
from App.ext import cache
from App.utlis import gen_movie_user_token


parse_base=reqparse.RequestParser()

parse_base.add_argument('action',type=str,required=True,help='请提供请求参数')
parse_base.add_argument('password',type=str,required=True,help='请输入密码')

parse_register=parse_base.copy()
parse_register.add_argument('username',type=str,required=True,help='请输入用户名')
parse_register.add_argument('phone',type=str,required=True,help='请输入电话号码')


parse_login=parse_base.copy()
parse_login.add_argument('username',type=str,help='请输入用户名')
parse_login.add_argument('phone',type=str,help='请输入电话号码')

movie_user_fields={
    'username':fields.String,
    'password':fields.String(attribute="_password"),
    'phone':fields.String
}
single_movie_user_fields={
    'status':fields.Integer,
    'msg':fields.String,
    'data':fields.Nested(movie_user_fields)

}


class MovieUserApis(Resource):

    def post(self):

        args=parse_base.parse_args()

        password = args.get('password')
        action = args.get('action')
        print(action)

        if action == USER_ACTION_REGISTER:
            args_register=parse_register.parse_args()
            username = args_register.get('username')
            phone = args_register.get('phone')

            movie_user=MovieUser()
            movie_user.username=username
            movie_user.password=password
            movie_user.phone=phone
            data = {
                'status': HTTP_CREATE_OK,
                'msg':'创建成功',
                'data':movie_user,
            }
            if not movie_user.save():
                abort(400)
            else:
                return marshal(data,single_movie_user_fields)
        elif action == USER_ACTION_LOGIN:
            args_login=parse_login.parse_args()
            username=args_login.get('username')
            phone=args_login.get('phone')

            user = get_users(username) or get_users(phone)

            if not user:
                abort(400,msg='用户不存在')
            if not user.check_password(password):
                abort(400,msg='密码错误')
            if user.is_delete:
                abort(401,msg='用户不存在')

            # 添加token
            token=gen_movie_user_token()
            cache.set(token,user.id,timeout=60*60*24*7)

            data={
                'msg':'login success',
                'status':HTTP_OK,
                'token':token,
            }
            return data
        else:
            abort(400)









