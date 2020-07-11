from flask import Flask
from .settings import envs
from .Apis import create_api
from App.ext import create_ext

def create_app(env):
    app=Flask(__name__,static_folder='../static',template_folder='../templates')


    app.config.from_object(envs.get(env))
    create_ext(app)
    create_api(app)

    return app