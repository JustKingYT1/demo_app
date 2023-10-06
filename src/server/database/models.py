from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    ID: int


class AccountPass(BaseModel):
    password: str


class SignIn(BaseModel):
    FIO: str

class AccountLog(AccountPass):
    userID: int
    login: str


class Accounts(BaseModel):
    userID: int
    login: str
    password: str


class UserAccount(Accounts):
    access_level: int

class Orders(ModifyBaseModel):
    accountID: int
    track_number: str
    total_cost: Optional[int] = None
    completed: bool = False


class OrderComplete(BaseModel):
    completed: bool


class ListProducts(BaseModel):
    orderID: int
    productID: int
    count: int


class ListProductsUpd(BaseModel):
    orderID: int
    productID: int
    count: int
    new_productID: int


class ListProductsDelOrGet(BaseModel):
    orderID: int
    productID: int


class RemnantsOfProducts(BaseModel):
    warehouseID: int
    productID: int
    count: int  

    
class UpdRemnantsOfProducts(RemnantsOfProducts):
    new_productID: int

