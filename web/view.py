from pprint import pprint
from sanic import text, response
from sanic.views import HTTPMethodView
from store.user.accessors import user_list, goods_list, account_list
from web.schemas import UserList, GoodList, AccountList


class AdminUserListView(HTTPMethodView):

    @staticmethod
    async def get(request):

        users_list = await user_list(request.app)
        pprint(UserList(userlist=users_list).json())
        return response.json(UserList(userlist=users_list).json())


class GoodsListView(HTTPMethodView):

    @staticmethod
    async def get(request):
        goods_lst = await goods_list(request.app)

        return response.json(GoodList(goodlist=goods_lst).json())


class UserAccountView(HTTPMethodView):

    @staticmethod
    async def get(request):
        account_lst = await account_list(request.app)
        pprint(account_lst)
        return response.json(AccountList(accountlist=account_lst).json())
