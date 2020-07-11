import uuid
from .adnis import ADMIS
from flask_restful import Resource,reqparse,abort,marshal,fields
from App.model.admin.admin_users_models import Admin_Users
from App.Apis.apis_contants import USER_ACTION_LOGIN,USER_ACTION_REGISTER,HTTP_CREATE_OK,HTTP_OK
from .admin_users_utils import get_users
from ...ext import cache
from App.utlis import gen_admin_user_token

parse_base=reqparse.RequestParser()
parse_base.add_argument('password',type=str,required=True,help='请输入密码')
parse_base.add_argument('action',type=str,required=True,help='请输入状态吗')
parse_base.add_argument('name',type=str,required=True,help='请输入用户名')


admin_users_fields={
    'name':fields.String,
    # '_password':fields.String(attribute='password'),
}
single_admin_users_fields={
    'msg':fields.String,
    'status':fields.Integer,
    'data':fields.Nested(admin_users_fields)
}


class Admin_Users_Apis(Resource):
    def post(self):
        args=parse_base.parse_args()
        password=args.get('password')
        action=args.get('action')
        if action == USER_ACTION_REGISTER:
            name=args.get('name')
            user=Admin_Users()
            user.name=name
            user.password=password

            if name in ADMIS:
                user.is_super = True

            if not user.save():
                abort(400,msg='create 失败')
            data={
                'msg':'创建成功',
                'status':HTTP_CREATE_OK,
                'data':user,
            }
            return marshal(data,single_admin_users_fields)


        elif action ==USER_ACTION_LOGIN:
            name=args.get('name')
            users=get_users(name)
            if not users:
                abort(400,msg='用户名错误')
            if not users.check_password(password):
                abort(400,msg='密码错误')

            if users.is_delete:
                abort(400, msg='用户名不存在')



            token=gen_admin_user_token()
            cache.set(token,users.id,timeout=60*60*24*7)
            data={
                'msg':'登录成功',
                'status':HTTP_OK,
                'token':token
            }
            return data


        else:
            abort(400,msg='亲 是不是什么写错拉？')



