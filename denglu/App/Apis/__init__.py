from flask_restful import Api
from .denglu import denglu
api=Api()

def create_api(app):
    api.init_app(app)

api.add_resource(denglu,'/denglu/')