import fastapi

from server.resolvers import warehouses


warehouses_router = fastapi.APIRouter(prefix='/warehouses', tags=["Warehouses"])


@warehouses_router.get(path='/get', response_model=dict)
def get_all_warehouses() -> dict:
    return warehouses.get_all()