

from sanic import Sanic, text

import store.database.sqlalchemy_base
# from sanic.log import logger
from store.database.database import Database
from store.user.accessors import user_list
from web.config import setup_config
from web.view import SimpleAsyncView

app = Sanic("MyTestApp")


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


@app.get("/users")
async def users(request):
    users_list = await user_list(app)
    return text("users")


def setup_database(app):
    app.ctx.db = Database(app)

    @app.listener('main_process_start')
    async def connect_to_db(*args, **kwargs):
        print('db connection established')
        await app.ctx.db.connect()

    @app.listener('main_process_stop')
    async def disconnect_from_db(*args, **kwargs):
        await app.ctx.db.disconnect()


app.add_route(SimpleAsyncView.as_view(), "/async")


def setup_app(config_path: str) -> Sanic:

    setup_config(app, config_path)
    setup_database(app)
    app.run(access_log=True, debug=True)
    return app
