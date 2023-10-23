import requests
from typing import Callable, Any
import sys

sys.path.append("C:\demo_app")

from src.server.database.models import Accounts, SignIn, AccountPass, ProductsGet

sys.path.append("C:\demo_app\src")

import settings


def server_available(func):
    def need_it(*args, **kwargs):
        try:
            requests.get(url=settings.URL)
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError as ex:
            return {"code": 400, "msg": str(ex), "error": True, "result": None}
    
    return need_it


@server_available
def delete_product_in_order(order_id: int, product_id: int) -> dict:
    return requests.delete(url=f'{settings.URL}/listProducts/delete/{order_id}/{product_id}').json()


@server_available
def add_product_in_cart(product_id: int, order_id: int, count: int) -> dict:
    return requests.post(url=f'{settings.URL}/listProducts/new', data=f'{{"orderID": "{order_id}", "productID": "{product_id}", "count": "{count}"}}').json()


@server_available
def complete_order(order_id: int) -> dict:
    return requests.put(url=f'{settings.URL}/orders/complete/{order_id}').json()


@server_available
def get_order(track_number: str, userID: int) -> None:
    return requests.post(url=f'{settings.URL}/orders/getOne', data=f'{{"track_number": "{track_number}", "userID": "{userID}"}}').json()


@server_available
def get_all_products_in_order(order_id: int) -> dict:
    return requests.get(url=f'{settings.URL}/listProducts/get/{order_id}').json()


@server_available
def get_access_level(user_id: int) -> int | dict:
    return requests.get(url=f'{settings.URL}/users/get/{user_id}').json()


@server_available
def get_all_products() -> dict:
    return requests.get(url=f"{settings.URL}/products/get").json()


@server_available
def get_userID(data: SignIn) -> dict:
    user = f'{{"FIO": "{data.FIO}"}}'
    return requests.post(url=f'{settings.URL}/accounts/sign', data=user).json()


@server_available
def register(user: Accounts) -> dict:
    data = f'{{"userID": "{user.userID}", "login": "{user.login}", "password": "{user.password}"}}'
    return requests.post(url=f'{settings.URL}/accounts/new', data=data).json()


@server_available
def login(user: Accounts) -> dict:
    data = f'{{"userID": "{user.userID}", "login": "{user.login}", "password": "{user.password}"}}'
    return requests.post(url=f'{settings.URL}/accounts/login', data=data).json()


@server_available
def update(password: AccountPass, userID: int) -> dict:
    data = f'{{"password": "{password.password}"}}'
    return requests.put(url=f"{settings.URL}/accounts/updatePassword/{userID}", data=data).json()


@server_available
def get_all_orders(userID: int) -> dict:
    return requests.get(url=f'{settings.URL}/orders/getAll/{userID}').json()


@server_available
def get_product(title: str) -> dict:
    return requests.post(url=f'{settings.URL}/products/get', data=f'{{"title": "{title}"}}').json()