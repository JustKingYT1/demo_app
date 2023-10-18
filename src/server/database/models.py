from pydantic import BaseModel
from typing import Optional
from datetime import date


class ModifyBaseModel(BaseModel):
    ID: int


class Users(ModifyBaseModel):
    typeID: int
    FIO: str
    phone: str
    date_birth: str


class AccountPass(BaseModel):
    password: str


class SignIn(BaseModel):
    FIO: str

class AccountLog(AccountPass):
    userID: int
    login: str


class ProductsGet(BaseModel):
    title: Optional[str]


class Products(ModifyBaseModel):
    title: str
    cost: int


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


class OrderTrackNum(BaseModel):
    track_number: str
    userID: int


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

