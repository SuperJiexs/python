from App.model import BaseModel
from App.ext import models


class Let_szm(BaseModel):
    let_szm=models.Column(models.String(2),unique=True)


class CityModel(BaseModel):
    let_szm_id=models.Column(models.Integer,models.ForeignKey(Let_szm.id))
    c_id=models.Column(models.Integer,default=0)
    c_parent_id=models.Column(models.Integer,default=0)
    c_name=models.Column(models.String(16))
    c_sitycode=models.Column(models.Integer,default=0)
    c_py=models.Column(models.String(128))
