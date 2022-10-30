from sqlalchemy import Integer, Column, VARCHAR, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from store.database.sqlalchemy_base import db
from web.schemas import User, Good, Account, Transaction


class UserModel(db):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(255), nullable=False, unique=True)
    password = Column(VARCHAR(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    active = Column(Boolean, default=False)
    accounts = relationship('AccountModel', backref='user_', lazy='immediate')

    def to_dc(self, account_flag: bool = False) -> User:
        return User(username=self.username,
                    password=self.password,
                    is_admin=self.is_admin,
                    active=self.active,
                    accounts=self.accounts if account_flag else None)


class GoodModel(db):
    __tablename__ = 'good'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(255), nullable=False, unique=True)
    description = Column(VARCHAR(255), nullable=False)
    cost = Column(Integer, nullable=False)

    def to_dc(self) -> Good:
        return Good(title=self.title,
                    description=self.description,
                    cost=self.cost)


class AccountModel(db):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    balance = Column(Integer, nullable=False)
    owner = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    transaction = relationship('TransactionModel', backref='transaction', lazy=True)

    def to_dc(self) -> Account:
        return Account(id=self.id,
                       balance=self.balance,
                       owner=self.owner
                       )


class TransactionModel(db):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    destination_account = Column(Integer, ForeignKey('account.id', ondelete='CASCADE'), nullable=False)
    # account = relationship(AccountModel, back_populates='account', lazy='immediate')

    def to_dc(self) -> Transaction:
        return Transaction(id=self.id,
                           amount=self.amount,
                           destination_account=self.destination_account)
