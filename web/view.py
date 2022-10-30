from hashlib import sha256
from pprint import pprint

from pydantic import ValidationError
from sanic import response
from sanic.exceptions import BadRequest, NotFound
from sanic.views import HTTPMethodView
from sqlalchemy import delete, update, select
from sqlalchemy.exc import IntegrityError

from store.user.accessors import user_list, goods_list, account_list, buy_good, new_transaction, user_with_account, activate_user
from store.user.models import GoodModel, UserModel
from web.schemas import UserList, GoodList, AccountList, BuySchema, TransactionSchema, UserWithAccountList, Good, ChangeUser, NewUser, User


class RegisterView(HTTPMethodView):

    @staticmethod
    async def post(request):
        try:
            user = NewUser(**request.json)
        except ValidationError as ve:
            return response.json(ve.json())
        await request.app.ctx.db.create_async_push_query(UserModel(username=user.username,
                                                                   password=sha256(user.password.encode()).hexdigest()
                                                                   ))
        return response.text(f'/user/newuser/{user.username}')


class LoginView(HTTPMethodView):

    @staticmethod
    async def post(request):
        try:
            user = NewUser(**request.json)
        except ValidationError as ve:
            raise BadRequest(message='Данные не верны')
        try:
            check_user: User = (
                await request.app.ctx.db.create_async_pull_query(select(UserModel)
                                                                 .where(UserModel.username == user.username))).scalar().to_dc()
        except AttributeError as e:
            raise NotFound(message=f'{user.username} is not found')
        if check_user.active and check_user.password == sha256(user.password.encode()).hexdigest():
            return response.text(f'Hello {user.username}')
        elif check_user.active is False:
            raise BadRequest(message='Учетная запись не активирована')
        else:
            raise BadRequest(message='Данные не верны')


class ActivateNewUserView(HTTPMethodView):

    @staticmethod
    async def get(request, name):
        await activate_user(request.app, name, status=True)
        return response.text('ok')


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


class BuyGoodView(HTTPMethodView):

    @staticmethod
    async def post(request):

        try:
            BuySchema(**request.json)
        except ValidationError as ve:
            return response.json(ve.json())

        res = await buy_good(app=request.app,
                             goodname=request.json['goodname'],
                             username=request.json['username'])
        return response.text(res)


class TransactionNewView(HTTPMethodView):

    @staticmethod
    async def post(request):
        try:
            tran = TransactionSchema(**request.json)
        except ValidationError as ve:
            return response.json(ve.json())
        if not tran.transaction_check(request.app):
            return response.text('Wrong transaction')
        res = await new_transaction(app=request.app,
                                    transaction=tran)
        return response.text(res)


class UserListWithAccountView(HTTPMethodView):

    @staticmethod
    async def get(request):
        usr_lst = await user_with_account(request.app)
        pprint(usr_lst)
        return response.json(UserWithAccountList(users=usr_lst).json())


class AdminEditGoodView(HTTPMethodView):

    @staticmethod
    async def get(request):
        goods_lst = await goods_list(request.app)
        return response.json(GoodList(goodlist=goods_lst).json())

    @staticmethod
    async def delete(request):
        try:
            good = Good(**request.json)
        except ValidationError as ve:
            return response.json(ve.json())
        query = delete(GoodModel).where(GoodModel.title == good.title)
        await request.app.ctx.db.create_async_update_query(query)
        return response.text('ok')

    @staticmethod
    async def put(request):
        try:
            good = Good(**request.json)
        except ValidationError as ve:
            return response.json(ve.json())
        await request.app.ctx.db.create_async_push_query(GoodModel(title=good.title,
                                                                   description=good.description,
                                                                   cost=good.cost))
        return response.text('ok')

    @staticmethod
    async def patch(request):
        try:
            good = Good(**request.json)
        except ValidationError as ve:
            return response.json(ve.json())
        await request.app.ctx.db.create_async_update_query(update(GoodModel)
                                                           .where(GoodModel.title == good.title)
                                                           .values(title=good.title,
                                                                   description=good.description,
                                                                   cost=good.cost))
        return response.text('ok')


class AdminChangeUserStatusView(HTTPMethodView):

    @staticmethod
    async def post(request):
        try:
            user = ChangeUser(**request.json)
        except ValidationError as ve:
            return response.json(ve.json())
        await activate_user(request.app, user.username, user.status)
        return response.text(f'{user.username} status is {"active" if user.status else "disable"}')
