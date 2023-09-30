import fastapi

from server.database.models import ListProducts, ListProductsDelOrGet, ListProductsUpd
from server.resolvers import list_products


listProducts_router = fastapi.APIRouter(prefix='/listProducts', tags=["ListProducts"])


@listProducts_router.get(path='/get/{order_id}', response_model=dict)
def get_list_products(order_id: int) -> dict:
    return list_products.get(order_id=order_id)

@listProducts_router.get(path='/get/{order_id}/{product_id}', response_model=dict)
def get_one_product_in_list_products_in_order(order_id: int, product_id: int) -> dict:
    return list_products.getOneProduct(order_id=order_id, product_id=product_id)


@listProducts_router.get(path='/get', response_model=dict)
def get_all_list_products_in_orders() -> dict:
    return list_products.get_all()


@listProducts_router.post(path='/new', response_model=dict)
def new_product_in_order(product: ListProducts) -> dict:
    return list_products.new(product=product)


@listProducts_router.put(path='/update', response_model=dict)
def update_order(new_product: ListProductsUpd) -> dict:
    return list_products.update(new_data=new_product)


@listProducts_router.delete(path='/delete/{order_id}/{product_id}', response_model=dict)
def delete_product_in_order(order_id: int, product_id: int) -> dict:
     return list_products.deleteOneProduct(order_id=order_id, product_id=product_id)


@listProducts_router.delete(path='/delete/{order_id}', response_model=dict)
def delete_product_in_order(order_id: int) -> dict:
     return list_products.delete(order_id=order_id)