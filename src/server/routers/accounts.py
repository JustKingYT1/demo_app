import fastapi

import sys

sys.path.append("C:/demo_app/src")
sys.path.append("C:/demo_app")

from src.server.database.models import Accounts, AccountPass, AccountLog, SignIn
from src.server.resolvers import accounts


accounts_router = fastapi.APIRouter(prefix='/accounts', tags=["Accounts"])


@accounts_router.get(path='/get/{user_id}', response_model=dict)
def get_account(user_id: int) -> dict:
    return accounts.get(user_id=user_id)


@accounts_router.post(path="/sign", response_model=dict)
def sign_in(data: SignIn) -> dict:
    return accounts.sign(data=data)

@accounts_router.get(path='/get', response_model=dict)
def get_all_accounts() -> dict:
    return accounts.get_all()


@accounts_router.post(path='/new', response_model=dict)
def new_account(account: Accounts) -> dict:
    return accounts.new(account=account)


@accounts_router.put(path='/updatePassword/{user_id}', response_model=dict)
def upd_pass(user_id: int, new_password: AccountPass) -> dict:
    return accounts.update(user_id=user_id, new_password=new_password)


@accounts_router.delete(path='/delete {user_id}', response_model=dict)
def delete_account(user_id: int) -> dict:
     return accounts.delete(user_id=user_id)


@accounts_router.post(path='/login', response_model=dict)
def account_login(account: AccountLog) -> dict:
    return accounts.login(account=account)