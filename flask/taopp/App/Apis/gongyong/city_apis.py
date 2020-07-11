from flask_restful import Resource, fields, marshal_with, marshal
from App.model.gongyong.city_model import CityModel,Let_szm
from App.Apis.apis_contants import HTTP_OK

city_fields={
    'c_id':fields.Integer(attribute='c_id'),
    'c_parent_id':fields.Integer(attribute='c_parent_id'),
    'c_name':fields.String(attribute='c_name'),
    'c_sitycode':fields.Integer(attribute='c_sitycode'),
    'c_py':fields.String(attribute='c_py')
}


class Citys(Resource):

    def get(self):

        let_szm=Let_szm.query.all()

        let_citys={}
        let_citys_fields={}
        for let in let_szm:
            let_city=CityModel.query.filter_by(let_szm_id=let.id)
            let_citys[let.let_szm]=let_city
            let_citys_fields[let.let_szm]=fields.List(fields.Nested(city_fields))
        data={
            'msg':'ok',
            'status':HTTP_OK,
            'data':marshal(let_citys,let_citys_fields),
        }


        return data