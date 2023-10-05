import fastapi

from server.resolvers import users


users_router = fastapi.APIRouter(prefix='/users', tags=["Users"])


@users_router.get(path='/get/{user_id}', response_model=dict)
def get_user(user_id: int) -> dict:
    return users.get(user_id=user_id)

