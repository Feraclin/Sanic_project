from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    is_admin: bool

    class Config:
        orm_mode = True


class Good(BaseModel):
    title: str
    description: str
    cost: int

    class Config:
        orm_mode = True


class Account(BaseModel):
    id: int
    balance: int
    owner: User

    class Config:
        orm_mode = True


class Transaction(BaseModel):
    amount: int
    destination_account: Account

    class Config:
        orm_mode = True
