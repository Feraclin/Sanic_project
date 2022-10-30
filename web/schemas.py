from hashlib import sha1
from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    is_admin: bool
    active: bool
    accounts: List | None = None

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
    owner: User | int

    class Config:
        orm_mode = True


class AccountWithTransaction(Account):
    transaction: Optional[List['Transaction']] = None


class AccountList(BaseModel):
    accountlist: List[Account]


class Transaction(BaseModel):
    id: int | None
    amount: int
    destination_account: Account | int

    class Config:
        orm_mode = True


class BuySchema(BaseModel):
    goodname: str
    username: str


class TransactionSchema(BaseModel):
    signature: str
    transaction_id: int
    user_id: int
    bill_id: int
    amount: int

    def to_dc(self) -> Transaction:
        return Transaction(id=self.transaction_id,
                           amount=self.amount,
                           destination_account=self.bill_id)

    def transaction_check(self, app) -> bool:
        return self.signature == sha1(f'{app.config.private_key}:{self.transaction_id}:{self.user_id}:{self.bill_id}:{self.amount}'.encode()).hexdigest()


class UserWithAccount(User):
    accounts: List[Account]


class UserWithAccountList(BaseModel):
    users: List[UserWithAccount]


class ChangeUser(BaseModel):
    username: str
    status: bool


class NewUser(BaseModel):
    username: str
    password: str