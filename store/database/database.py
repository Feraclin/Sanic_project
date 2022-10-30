from typing import TYPE_CHECKING, Optional
from sanic.log import logger
from sqlalchemy.engine import URL
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from store.database.sqlalchemy_base import db
from store.user.accessors import create_admin_user

if TYPE_CHECKING:
    from sanic import Sanic


class Database:

    def __init__(self, app: "Sanic"):
        self.app = app
        self.DATABASE_URL = URL.create(drivername='postgresql+asyncpg',
                                       host=app.config.db_config.host,
                                       database=app.config.db_config.database,
                                       username=app.config.db_config.user,
                                       password=app.config.db_config.password,
                                       port=app.config.db_config.port)
        self._engine: Optional[AsyncEngine] = None
        self._db: Optional[declarative_base] = None
        self.session: Optional[sessionmaker] = None

    async def connect(self, *_: list, **__: dict) -> None:
        print('connect to db')
        self._db = db

        self._engine = create_async_engine(self.DATABASE_URL, echo=False, future=True)

        self.session = sessionmaker(bind=self._engine,
                                    expire_on_commit=False,
                                    autoflush=True,
                                    class_=AsyncSession)

        try:
            await create_admin_user(username=self.app.config.default_admin.name,
                                    password=self.app.config.default_admin.password,
                                    app=self.app)
        except IntegrityError:
            logger.info("Admin already exists")

    async def create_async_pull_query(self, query):
        async with self.session() as session:

            res = await session.execute(query)
            await session.commit()
        await self._engine.dispose()
        return res

    async def create_async_push_query(self, modification_variable):

        async with self.session.begin() as session:

            if type(modification_variable) is list:
                session.add_all(modification_variable)
            else:

                session.add(modification_variable)
            await session.commit()

        await self._engine.dispose()

    async def create_async_update_query(self, query):

        async with self.session.begin() as session:
            res = await session.execute(query)
            await session.commit()
            return res

    async def create_async_merge_query(self, query):

        async with self.session.begin() as session:
            res = await session.merge(query)
            await session.commit()
            return res

    async def disconnect(self, *_: list, **__: dict) -> None:
        try:
            await self._engine.dispose()
        except Exception as e:
            logger.info(f'Disconnect from engine error {e}')
