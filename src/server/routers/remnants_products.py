import fastapi

from server.database.models import RemnantsOfProducts, DelRemnantsOfProducts
from server.resolvers import remnants_products


remnants_router = fastapi.APIRouter(prefix='/remnants', tags=["Orders"])


@remnants_router('/')
def start_page() -> dict:
    return f"Hello user"


@remnants_router.get(path='/{warehouseID}/get', response_model=dict)
def get_remnants_on_warhouse(warehouseID: int) -> dict:
    return remnants_products.get(warehouse_id=warehouseID)


@remnants_router.get(path='/get', response_model=dict)
def get_all_remnants_on_all_warehouses() -> dict:
    return remnants_products.get_all()


@remnants_router.post(path='/new', response_model=dict)
def new_product_on_warehouse(product: RemnantsOfProducts) -> dict:
    return remnants_products.new(product=product)


@remnants_router.put(path='/update', response_model=dict)
def update_product_on_warehouse(new_data: RemnantsOfProducts) -> dict:
    return remnants_products.complete(new_data=new_data)


@remnants_router.delete(path='/delete', response_model=dict)
def delete_product_on_warehouse(data: DelRemnantsOfProducts) -> dict:
     return remnants_products.delete(data=data)