from functools import wraps

import jwt
from sanic import text
from sanic.exceptions import Forbidden
from sqlalchemy import select

from store.user.models import UserModel


def check_token(request):
    if not request.token:
        return False

    try:
        jwt.decode(
            request.token, request.app.config.secret, algorithms=["HS256"]
        )
    except jwt.exceptions.InvalidTokenError:
        return False
    else:
        return True


def protected(wrapped):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authenticated = check_token(request)

            if is_authenticated:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return text("You are unauthorized.", 401)

        return decorated_function

    return decorator(wrapped)


def protected_admin(wrapped: object) -> object:
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authenticated = check_token(request)

            if is_authenticated:

                user = await logged_user(request)
                if user.is_admin:
                    response = await f(request, *args, **kwargs)
                    return response
                else:
                    return text("Forbidden", 403)
            else:
                return text("You are unauthorized.", 401)

        return decorated_function

    return decorator(wrapped)


async def logged_user(request):
    username = jwt.decode(request.token, request.app.config.secret, algorithms=["HS256"]).get('name')
    user = (await request.app.ctx.db.create_async_pull_query(select(UserModel)
                                                             .where(UserModel.username == username))).scalar().to_dc()
    return user
