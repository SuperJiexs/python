from flask_restful import Api
from .admin_users import Admin_Users_Apis


admin_api=Api(prefix='/ad')

admin_api.add_resource(Admin_Users_Apis,'/users/')