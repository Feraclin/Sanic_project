from hashlib import sha256
from pprint import pprint
from typing import TYPE_CHECKING, List

from sqlalchemy import select

from store.user.models import UserModel
from web.schemas import User


async def create_admin_user(username: str, password: str, app) -> User:
    admin = UserModel(username=username,
                      password=sha256(password.encode()).hexdigest(),
                      is_admin=True)

    await app.ctx.db.create_async_push_query(admin)

    return admin.to_dc()


async def user_list(app) -> List[User] | None:
    query = select(UserModel)
    print('error')
    res = await app.ctx.db.create_async_pull_query(query)
    pprint(res)
    if not res:
        return None

    return [i.to_dc() for i in res]
