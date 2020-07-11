from flask_restful import Api

from .movie_user_apis import MovieUserApis
from .movie_order_apis import MovieOrdersApis,MovieOrderApis

client_api=Api(prefix='/cl')

client_api.add_resource(MovieUserApis,'/mua/')
client_api.add_resource(MovieOrdersApis,'/mosa/')
client_api.add_resource(MovieOrderApis,'/moa/<int:order_id>')