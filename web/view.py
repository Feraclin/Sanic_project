from sanic import text
from sanic.views import HTTPMethodView


class SimpleAsyncView(HTTPMethodView):
    async def get(self, request):
        return text("I am async get method")

    async def post(self, request):
        return text("I am async post method")

    async def put(self, request):
        return text("I am async put method")
