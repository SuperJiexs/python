from flask_restful import Api
from .city_apis import Citys
from .movie_dy import Movies_dy,Movie_dy,Moviesdy,Moviesremen


gongyong_api=Api(prefix='/ct')

gongyong_api.add_resource(Citys,'/citys/')
gongyong_api.add_resource(Movies_dy,'/dys/')
gongyong_api.add_resource(Movie_dy,'/dy/<string:name>/')
gongyong_api.add_resource(Moviesdy,'/mdy/<int:id>/')
gongyong_api.add_resource(Moviesremen,'/mvrm/')





