import fastapi

from server.database.models import Orders, OrderComplete, OrderTrackNum
from server.resolvers import orders


orders_router = fastapi.APIRouter(prefix='/orders', tags=["Orders"])


@orders_router.post(path='/getOne', response_model=dict)
def get_order(order: OrderTrackNum) -> dict:
    return orders.get(order=order)


@orders_router.get(path='/getAll/{userID}', response_model=dict)
def get_all_orders(userID: int) -> dict:
    return orders.get_all(accountID=userID)

@orders_router.post(path='/new', response_model=dict)
def new_order(order: Orders) -> dict:
    return orders.new(order=order)


@orders_router.put(path='/complete/{order_id}', response_model=dict)
def complete_order(order_id: int, new_data: OrderComplete) -> dict:
    return orders.complete(orderID=order_id, new_data=new_data)


@orders_router.delete(path='/delete/{order_id}', response_model=dict)
def delete_order(order_id: int) -> dict:
     return orders.delete(orderID=order_id)