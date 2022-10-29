from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    is_admin: bool
    account: Optional[List['Good']] = None

    class Config:
        orm_mode = True


class UserList(BaseModel):
    userlist: List[User]


class Good(BaseModel):
    title: str
    description: str
    cost: int

    class Config:
        orm_mode = True


class GoodList(BaseModel):
    goodlist: List[Good]


class Account(BaseModel):
    id: int
    balance: int
    owner: User
    transaction: Optional[List['Transaction']] = None

    class Config:
        orm_mode = True


class AccountList(BaseModel):
    accountlist: List[Account]


class Transaction(BaseModel):
    amount: int
    destination_account: Account

    class Config:
        orm_mode = True
