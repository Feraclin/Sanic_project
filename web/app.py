from pprint import pprint

from sanic import Sanic

from store.database.database import Database

from web.config import setup_config
from web.routes import setup_blueprints


def setup_app(name: str, config_path: str) -> Sanic:
    api = Sanic(name)
    setup_config(api, config_path)
    setup_database(api)
    setup_blueprints(api)
    return api


def setup_database(app):
    app.ctx.db = Database(app)

    @app.listener('before_server_start')
    async def connect_to_db(*args, **kwargs):
        print('db connection established')
        await app.ctx.db.connect()

    @app.listener('after_server_stop')
    async def disconnect_from_db(*args, **kwargs):
        await app.ctx.db.disconnect()
