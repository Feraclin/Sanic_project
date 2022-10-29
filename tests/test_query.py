import asyncio
from pprint import pprint

from sqlalchemy import select
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from store.user.models import AccountModel, TransactionModel, UserModel

engine = create_async_engine(
    URL(
        drivername="postgresql+asyncpg",
        host='localhost',
        database='sanic_test',
        username='feraclin',
        password='12wm16ln',
        port=5433,
    ),
    echo=False,
    future=True,
)

session = sessionmaker(bind=engine,
                       expire_on_commit=False,
                       autoflush=True,
                       class_=AsyncSession)


async def create_async_pull_query(query, session, engine):
    async with session() as session:
        res = await session.execute(query)
        await session.commit()
    await engine.dispose()
    # [pprint(line.__dict__['account'].__dict__['user'].__dict__) for line in res.scalars().all()]
    # pprint([line.to_dc() for line in res.scalars().all()])
    [pprint(line.__dict__['account'].__dict__['user'].__dict__) for line in res.scalars().all()]

if __name__ == "__main__":

    query = select(AccountModel, TransactionModel) \
        .join(TransactionModel, AccountModel.id == TransactionModel.destination_account)
    query1 = select(AccountModel, UserModel) \
        .join(UserModel, AccountModel.owner == UserModel.id)
    query2 = select(TransactionModel, AccountModel, UserModel)\
        .join(AccountModel, TransactionModel.destination_account == AccountModel.id)\
        .join(UserModel, AccountModel.owner == UserModel.id)
    query4 = select(AccountModel)
    asyncio.run(create_async_pull_query(query=query4,
                                        session=session,
                                        engine=engine))
