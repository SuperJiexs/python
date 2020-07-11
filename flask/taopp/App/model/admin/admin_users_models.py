from werkzeug.security import generate_password_hash, check_password_hash
from App.ext import models


from App.model import BaseModel
PERMISSION_NONE=0
PERMISSION_MAN=1
class Admin_Users(BaseModel):
    name = models.Column(models.String(32), unique=True)
    _password = models.Column(models.String(256))

    is_delete = models.Column(models.Boolean(), default=False)
    is_super = models.Column(models.Boolean(), default=False)
    permission = models.Column(models.Integer, default=PERMISSION_NONE)

    @property
    def password(self):
        raise Exception('不准查看')

    @password.setter
    def password(self, password_value):
        self._password = generate_password_hash(password_value)

    def check_password(self, user_password):
        return check_password_hash(self._password, user_password)

    def check_permission(self, permission_s):
        return self.is_super or self.permission & permission_s == permission_s




