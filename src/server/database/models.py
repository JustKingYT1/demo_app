from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    id: int


class AccountPass(ModifyBaseModel):
    password: str


class AccountLog(ModifyBaseModel):
    login: str


class Accounts(AccountPass, AccountLog):
    userID: int


class Orders(ModifyBaseModel):
    accountID: int
    track_number: str
    total_cost: Optional[int] = None
    completed: bool = False


class OrderComplete(ModifyBaseModel):
    completed: bool


class ListProducts(ModifyBaseModel):
    orderID: int
    productID: int
    count: int


class ProductUpd(ListProducts):
    new_productID: int


class ProductDel(ListProducts):
    count: Optional[int]


class DelRemnantsOfProducts(ModifyBaseModel):
    count: int

class RemnantsOfProducts(DelRemnantsOfProducts):
    warehouseID: int
    productID: int