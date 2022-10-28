import asyncio

from sanic import Sanic
from sanic.response import text
from sanic.views import HTTPMethodView

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


class SimpleAsyncView(HTTPMethodView):
    async def get(self, request):
        return text("I am async get method")

    async def post(self, request):
        return text("I am async post method")

    async def put(self, request):
        return text("I am async put method")


app.add_route(SimpleAsyncView.as_view(), "/async")


if __name__ == "__main__":
    app.run()
