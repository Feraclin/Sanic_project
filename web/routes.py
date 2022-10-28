from typing import TYPE_CHECKING

from web.view import SimpleAsyncView
if TYPE_CHECKING:
    from sanic import Sanic


def setup_routes(app: "Sanic") -> None:
    app.add_route(SimpleAsyncView.as_view(), "/async")

