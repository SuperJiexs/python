from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache
from flask_mail import Mail


mail=Mail()
models=SQLAlchemy()
migrate=Migrate()
toolbar=DebugToolbarExtension()
cache=Cache(config={
    "CACHE_TYPE":"redis"
})



def create_ext(app):
    models.init_app(app)
    migrate.init_app(app,models)
    Session(app)
    Bootstrap(app)
    toolbar.init_app(app)
    cache.init_app(app)
    mail.init_app(app)





