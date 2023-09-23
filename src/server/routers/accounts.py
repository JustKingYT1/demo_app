import fastapi

from server.database.models import Accounts, AccountPass, AccountLog
from server.resolvers import accounts


accounts_router = fastapi.APIRouter(prefix='/accounts', tags=["Accounts"])


@accounts_router('/')
def start_page() -> dict:
    return f"Hello user"


@accounts_router.get(path='/{user_id}/get', response_model=dict)
def get_account(user_id: int) -> dict:
    return accounts.get(user_id=user_id)


@accounts_router.get(path='/get', response_model=dict)
def get_all_accounts() -> dict:
    return accounts.get_all()


@accounts_router.post(path='/create', response_model=dict)
def new_account(account: Accounts) -> dict:
    return accounts.new(account=account)


@accounts_router.put(path='/{user_id}/updateLogin', response_model=dict)
def upd_log(user_id: int, new_login: AccountLog) -> dict:
    return accounts.update_login(user_id=user_id, new_login=new_login)


@accounts_router.put(path='/{user_id}/updatePassword', response_model=dict)
def upd_pass(user_id: int, new_password: AccountPass) -> dict:
        return accounts.update_password(user_id=user_id, new_password=new_password)


@accounts_router.delete(path='/{user_id}/delete', response_model=dict)
def delete_account(user_id: int) -> dict:
     return accounts.delete(user_id=user_id)