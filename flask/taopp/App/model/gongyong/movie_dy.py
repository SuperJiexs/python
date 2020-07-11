from App.model import BaseModel
from App.ext import models


class movies_dy(BaseModel):
    __tablename__='dy'
    dy_name=models.Column(models.String(64))
    dy_id=models.Column(models.Integer)
    dy_daoyan=models.Column(models.String(64))
    dy_zhuyan=models.Column(models.String(256))
    by_type=models.Column(models.String(64))
    dy_country=models.Column(models.String(64))
    dy_yuyan=models.Column(models.String(64))
    dy_pianchang=models.Column(models.Integer,default=120)
    dy_riqi=models.Column(models.DateTime)
    dy_img=models.Column(models.String(256))
    dy_desc=models.Column(models.String(1248))
    dy_xiazai=models.Column(models.String(128))
    flag=models.Column(models.Boolean,default=False)
    is_del=models.Column(models.Boolean,default=False)







