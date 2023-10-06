import requests
from typing import Callable, Any
import sys

sys.path.append("C:\demo_app")

from src.server.database.models import Accounts, SignIn, AccountPass

sys.path.append("C:\demo_app\src")

import settings


def server_available(func: Callable) -> Callable:
    def need_it(*args, **kwargs) -> Callable:
        try:
            requests.get(url=settings.URL)
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError as ex:
            return {"code": 400, "msg": str(ex), "error": True, "result": None}
    
    return need_it

@server_available
def get_access_level(user_id: int) -> int | dict:
    return requests.get(url=f'{settings.URL}/users/get/{user_id}').json()

@server_available
def get_userID(data: SignIn) -> dict:
    return requests.post(url=f'{settings.URL}/accounts/sign', data=data).json()

@server_available
def register(user: Accounts) -> dict:
    return requests.post(url=f'{settings.URL}/accounts/new', data=user).json()

@server_available
def login(user: Accounts) -> dict:
    return requests.post(url=f'{settings.URL}/accounts/login', data=user).json()

@server_available
def update(password: AccountPass, userID: int) -> dict:
    return requests.put(url=f"{settings.URL}/accounts/updatePassword/{userID}", data=password).json()