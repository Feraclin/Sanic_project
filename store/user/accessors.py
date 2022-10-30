from hashlib import sha256
from pprint import pprint
from typing import List

from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError

from store.user.models import UserModel, GoodModel, AccountModel, TransactionModel
from web.schemas import User, Good, Account, TransactionSchema, UserWithAccount


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
        query = select(AccountModel, TransactionModel) \
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


async def change_account_balance(app, account_id: str, amount: int):
    query = update(AccountModel).where(AccountModel.id == account_id).values(balance=AccountModel.balance - amount)
    await app.ctx.db.create_async_update_query(query)


async def buy_good(app, goodname: str, username: str) -> str:
    query = select(GoodModel).where(GoodModel.title == goodname)
    good = (await app.ctx.db.create_async_pull_query(query)).scalar()
    if not good:
        return f'Товар {goodname} отсутсвует'
    else:
        good = good.to_dc()
    query = select(AccountModel).join(UserModel, AccountModel.owner == UserModel.id).where(UserModel.username == username)
    balance = (await app.ctx.db.create_async_pull_query(query)).scalars().all()
    if not balance:
        return f'У {username} отсутвует счет'
    balance_lst = [i.to_dc() for i in balance]
    for i in balance_lst:
        if i.balance >= good.cost:
            await change_account_balance(app, i.id, good.cost)
            return f'Товар {goodname} приобретен'
    return f'У {username} недостаточно средств на {goodname}'


async def new_transaction(app, transaction: TransactionSchema) -> str:
    check_transaction = select(TransactionModel).where(TransactionModel.id == transaction.transaction_id)
    if (await app.ctx.db.create_async_pull_query(check_transaction)).scalar():
        return 'Transaction already in base'
    new_tran = TransactionModel(id=transaction.transaction_id,
                                amount=transaction.amount,
                                destination_account=transaction.bill_id)
    try:
        await app.ctx.db.create_async_push_query(new_tran)
        query = update(AccountModel).where(AccountModel.id == transaction.bill_id)\
            .values(balance=AccountModel.balance + new_tran.amount)
        await app.ctx.db.create_async_update_query(query)
        return 'Transaction completed successfully with old bill'
    except IntegrityError as e:
        match e.orig.pgcode:
            case '23503':
                query = AccountModel(id=transaction.bill_id,
                                     balance=transaction.amount,
                                     owner=transaction.user_id)
                await app.ctx.db.create_async_push_query(query)
                await app.ctx.db.create_async_push_query(new_tran)
                return 'Transaction completed successfully with new bill'


async def user_with_account(app) -> List:
    query = select(UserModel).join(AccountModel, UserModel.id == AccountModel.owner).order_by(UserModel.username)
    usr_lst = await app.ctx.db.create_async_pull_query(query)
    usr_lst = [UserWithAccount(**line.__dict__) for line in usr_lst.scalars().all()]
    usr_dct = {}
    for i in usr_lst:
        if i.username not in usr_dct:
            usr_dct[i.username] = i
        else:
            usr_dct.get(i.username).accounts.extend(i.accounts)

    return list(usr_dct.values())


async def activate_user(app, username, status):
    await app.ctx.db.create_async_update_query(update(UserModel)
                                               .where(UserModel.username == username)
                                               .values(active=status))
