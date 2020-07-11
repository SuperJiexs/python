from .movie_user import client_api
from .admin import admin_api
from .movie_admin import movie_client_api
from .gongyong import gongyong_api

def create_api(app):
    client_api.init_app(app)
    movie_client_api.init_app(app)
    admin_api.init_app(app)
    gongyong_api.init_app(app)