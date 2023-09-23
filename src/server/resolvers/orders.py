from database.db_manager import db_manager

from database.models import Orders, OrderComplete

def new(order: Orders) -> dict:
    res = db_manager.execute(query="""INSERT INTO Orders(accountID, track_number, total_cost, completed) 
                                          VALUES(?, ?, ?, ?) 
                                          RETURNING ID""", 
                              args=(order.accountID, order.track_number, order.total_cost, order.completed))
    
    res["result"] = None if not res["result"] else get(res["result"][0])

def get(order_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Orders 
                                       WHERE ID = ?""", 
                              args=(order_id,)) 
    
    res["result"] = None if not res["result"] else Orders(
        id=res["result"][0],
        accountID=res["result"][1],
        track_number=res["result"][2],
        total_cost=res["result"][3],
        completed=res["result"][4]
    )

    return res

def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Orders""", 
                              many=True)

    list_orders = []

    if res["result"]:
        for order in res["result"]:
            list_orders.append(Orders(
                id=order["result"][0],
                accountID=order["result"][1],
                track_number=order["result"][2],
                total_cost=order["result"][3],
                completed=order["result"][4]
            ))
        res["result"] = list_orders
    else:
        res["result"] = None

    return res

def complete(orderID: int, new_data: OrderComplete) -> dict:
    res = db_manager.execute(query="""UPDATE Orders(completed) 
                                       SET (?) 
                                       WHERE (orderID) = (?)
                                       RETURNING ID""",
                              args=(new_data.completed, orderID))
    
    res["msg"] = None if not res["result"] else "Completed"
    res["result"] = None if not res["result"] else get(res["result"][0])


def delete(orderID: int) -> dict:
    return db_manager.execute(query="""DELETE FROM Orders WHERE ID = ? """,
                              args=(orderID))