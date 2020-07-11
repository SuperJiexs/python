from App.model import BaseModel
from App.ext import models
from werkzeug.security import generate_password_hash,check_password_hash
from .models_constant import PERMISSION_NONE

BLACK_USER = 1
COMMOM_USER = 0
VIP_USER = 2


class MovieUser(BaseModel):
    username=models.Column(models.String(32),unique=True)
    _password=models.Column(models.String(256))
    phone=models.Column(models.String(32),unique=True)
    # 逻辑删除
    is_delete=models.Column(models.Boolean,default=False)
    permission=models.Column(models.Integer,default=PERMISSION_NONE)




    @property
    def password(self):
        raise Exception('no password')

    @password.setter
    def password(self,passwords):
        self._password=generate_password_hash(passwords)

    def check_password(self,password_v):
        return check_password_hash(self._password,password_v)



    def check_permission(self,permission):
        if BLACK_USER & self.permission == BLACK_USER:
            return False
        else:
            return permission & self.permission == permission



