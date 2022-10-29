from hashlib import sha256
from pprint import pprint
from typing import TYPE_CHECKING, List

from sqlalchemy import select

from store.user.models import UserModel, GoodModel, AccountModel, TransactionModel
from web.schemas import User, Good, Account


async def create_admin_user(username: str, password: str, app) -> User:
    admin = UserModel(username=username,
                      password=sha256(password.encode()).hexdigest(),
                      is_admin=True,
                      active=True)

    await app.ctx.db.create_async_push_query(admin)

    return admin.to_dc()


async def user_list(app) -> List[User] | None:
    try:
        query = select(UserModel)

        res = (await app.ctx.db.create_async_pull_query(query)).scalars().all()

        if not res:
            return None

        return [i.to_dc() for i in res]
    except Exception as e:
        print(e)
        print("Error creating pull user list")


async def goods_list(app) -> List[Good] | None:
    try:
        query = select(GoodModel)
        res = (await app.ctx.db.create_async_pull_query(query)).scalars().all()

        if not res:
            return None

        return [i.to_dc() for i in res]

    except Exception as e:
        print(e)
        print("Error creating pull good list")


async def account_list(app) -> List[Account] | None:
    try:
        query = select(AccountModel, TransactionModel)\
            .join_from(AccountModel, TransactionModel, AccountModel.id == TransactionModel.destination_account)
        res = (await app.ctx.db.create_async_pull_query(query)).scalars().all()

        if not res:
            return None
        pprint(res[0])
        [pprint(i.__dict__) for i in res]
        return [i.to_dc() for i in res]

    except Exception as e:
        print(e)
        print("Error creating pull account list")
