from flask_restful import Resource,reqparse,abort,fields,marshal,request,marshal_with
from App.Apis.apis_contants import HTTP_CREATE_OK, HTTP_OK
from App.model.gongyong.movie_dy import movies_dy
from App.Apis.admin.admin_utils import login_required
from App.settings import STATIC_IMG,IMG_PATH
from flask_pagination import Pagination


parse=reqparse.RequestParser()
'''
 dy_name=models.Column(models.String(64))
    dy_b_name=models.Column(models.String(128))
    dy_daoyan=models.Column(models.String(64))
    dy_zhuyan=models.Column(models.String(256))
    by_type=models.Column(models.String(64))
    dy_country=models.Column(models.String(64))
    dy_yuyan=models.Column(models.String(64))
    dy_pianchang=models.Column(models.Integer,default=120)
    dy_riqi=models.Column(models.DateTime)
    dy_img=models.Column(models.String(256))
    dy_desc=models.Column(models.String(1248))
    flag=models.Column(models.Boolean,default=False)
    is_del=models.Column(models.Boolean,default=False)
'''

parse.add_argument('dy_name',required=True,help='请输入电影名字')
parse.add_argument('dy_id',required=True,help='请输入电影别名')
parse.add_argument('dy_daoyan',required=True,help='请输入电影导演')
parse.add_argument('dy_zhuyan',required=True,help='请输入电影主演')
parse.add_argument('by_type',required=True,help='请输入电影类型')
parse.add_argument('dy_country',required=True,help='请输入电影国家')
parse.add_argument('dy_yuyan',required=True,help='请输入电影语言')
parse.add_argument('dy_pianchang',required=True,help='请输入电影时长')
parse.add_argument('dy_riqi',required=True,help='请输入电影上映日期')
parse.add_argument('dy_xiazai',required=True,help='请输入电影下载地址')
# parse.add_argument('dy_img',required=True,help='请输入电影图片',location=['files'])
parse.add_argument('dy_desc',required=True,help='请输入电影简介')


movie_dy_fields={
    'dy_name': fields.String,
    'dy_id': fields.Integer,
    'dy_daoyan': fields.String,
    'dy_zhuyan': fields.String,
    'by_type': fields.String,
    'dy_country': fields.String,
    'dy_yuyan': fields.String,
    'dy_pianchang': fields.Integer,
    'dy_riqi': fields.DateTime,
    'dy_img': fields.String,
    'dy_desc': fields.String,
    'dy_xiazai': fields.String,

}

single_movie_dy_fields={
    'status':fields.Integer,
    'msg':fields.String,
    'data':fields.Nested(movie_dy_fields)
}





class Movies_dy(Resource):
    @marshal_with(single_movie_dy_fields)
    def get(self):
        movie=movies_dy.query.all()

        data={
            'status': HTTP_OK,
            'msg': '电影表单',
            'data': movie,
        }


        return data

    @login_required
    def post(self):
        args=parse.parse_args()

        # 接受参数
        dy_name=args.get('dy_name')
        dy_id = args.get('dy_id')
        dy_daoyan = args.get('dy_daoyan')
        dy_zhuyan = args.get('dy_zhuyan')
        by_type = args.get('by_type')
        dy_country = args.get('dy_country')
        dy_yuyan = args.get('dy_yuyan')
        dy_pianchang = args.get('dy_pianchang')
        dy_riqi = args.get('dy_riqi')
        # dy_img = args.get('dy_img')
        dy_desc = args.get('dy_desc')
        dy_xiazai = args.get('dy_xiazai')

        dy_img=request.files.get('dy_img')

        movie_dy=movies_dy()

        movie_dy.dy_name=dy_name
        movie_dy.dy_id = dy_id
        movie_dy.dy_daoyan = dy_daoyan
        movie_dy.dy_zhuyan = dy_zhuyan
        movie_dy.by_type = by_type
        movie_dy.dy_country = dy_country
        movie_dy.dy_yuyan = dy_yuyan
        movie_dy.dy_pianchang = dy_pianchang
        movie_dy.dy_riqi = dy_riqi
        movie_dy.dy_desc = dy_desc
        movie_dy.dy_xiazai = dy_xiazai

        filepath=STATIC_IMG+'/'+dy_img.filename
        dy_img.save(filepath)
        movie_dy.dy_img=IMG_PATH+'/'+dy_img.filename

        if not movie_dy.save():
            abort(400,msg='创建失败')
        data={
            'status': HTTP_CREATE_OK,
            'msg': '创建成功',
            'data': movie_dy,
        }

        return marshal(data,single_movie_dy_fields)

class Movie_dy(Resource):
    def get(self,name):
        print(name)
        movies=movies_dy.query.filter(movies_dy.dy_name.like("%"+name+"%")).all()
        if not movies:
            data = {
                'status': '401',
                'msg': '查询不到相关的信息',
            }
            return data
        data = {
            'status': HTTP_CREATE_OK,
            'msg': '查询成功',
            'data': movies,
        }
        return marshal(data,single_movie_dy_fields)


    @login_required
    def patch(self,id):

        return {'msg':'patch ok'}

    @login_required
    def put(self, id):
        return {'msg': 'put ok'}

    @login_required
    def delete(self, id):
        return {'msg': 'delete ok'}


class Moviesdy(Resource):
    def get(self,id):
        moviesdy=movies_dy.query.filter(movies_dy.dy_id.__eq__(id)).all()

        data={
            'status': HTTP_CREATE_OK,
            'msg': '查询成功',
            'data': moviesdy,
        }
        return marshal(data,single_movie_dy_fields)


class Moviesremen(Resource):
    def get(self):

        moviesremen=movies_dy.query.filter(movies_dy.flag.__eq__(1)).all()


        data={
            'status': HTTP_CREATE_OK,
            'msg': '查询成功',
            'data': moviesremen,
        }
        return marshal(data,single_movie_dy_fields)




