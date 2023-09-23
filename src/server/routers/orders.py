import fastapi

from server.database.models import Orders, OrderComplete
from server.resolvers import orders


orders_router = fastapi.APIRouter(prefix='/orders', tags=["Orders"])


@orders_router('/')
def start_page() -> dict:
    return f"Hello user"


@orders_router.get(path='{order_id}/get', response_model=dict)
def get_list_products(order_id: int) -> dict:
    return orders.get(order_id=order_id)


@orders_router.get(path='/get', response_model=dict)
def get_all_orders() -> dict:
    return orders.get_all()


@orders_router.post(path='/new', response_model=dict)
def new_order(order: Orders) -> dict:
    return orders.new(order=order)


@orders_router.put(path='/{orderID}/complete', response_model=dict)
def complete_order(orderID: int, new_data: OrderComplete) -> dict:
    return orders.complete(orderID=orderID, new_data=new_data)


@orders_router.delete(path='/{orderID}/delete', response_model=dict)
def delete_order(orderID: int) -> dict:
     return orders.delete(orderID=orderID)