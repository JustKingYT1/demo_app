import fastapi

from server.database.models import RemnantsOfProducts
from server.resolvers import remnants_products


remnants_router = fastapi.APIRouter(prefix='/remnants', tags=["Remnants"])


@remnants_router.get(path='/get/{warehouseID}', response_model=dict)
def get_remnants_on_warhouse(warehouseID: int) -> dict:
    return remnants_products.get(warehouse_id=warehouseID)


@remnants_router.get(path='/get/{warehouseID}/{productID}', response_model=dict)
def get_remnants_of_product_on_warhouse(warehouseID: int, productID: int) -> dict:
    return remnants_products.getOneProduct(warehouse_id=warehouseID, productID=productID)


@remnants_router.get(path='/get', response_model=dict)
def get_all_remnants_on_all_warehouses() -> dict:
    return remnants_products.get_all()


@remnants_router.post(path='/new', response_model=dict)
def new_product_on_warehouse(product: RemnantsOfProducts) -> dict:
    return remnants_products.new(product=product)


@remnants_router.put(path='/update', response_model=dict)
def update_product_on_warehouse(new_data: RemnantsOfProducts) -> dict:
    return remnants_products.update(new_data=new_data)


@remnants_router.delete(path='/delete/{warehouseID}/{productID}', response_model=dict)
def delete_product_on_warehouse(warehouseID: int, productID: int) -> dict:
     return remnants_products.delete(warehouseID=warehouseID, productID=productID)