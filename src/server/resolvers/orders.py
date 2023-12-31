from server.database.db_manager import db_manager

from server.database.models import Orders, TotalCost, OrderTrackNum

def new(order: Orders) -> dict:
    res = db_manager.execute(query="""INSERT INTO Orders(ID, accountID, trackNumber, totalCost, completed) 
                                          VALUES(?, ?, ?, ?, ?) 
                                          RETURNING ID""", 
                              args=(order.ID, order.accountID, order.track_number, order.total_cost, order.completed))
    
    # res["result"] = None if not res["result"] else get(res["result"][0])["result"]

    return res

# def set_total_cost(order_id: int, total_cost: TotalCost) -> dict:
#     res = db_manager.execute(query='''UPDATE Orders SET totalCost = ? WHERE ID = ?''',
#                              args=(total_cost.total_cost, order_id))
    
#     return res

def get(order: OrderTrackNum) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Orders 
                                       WHERE trackNumber = ? AND accountID = ?""", 
                              args=(order.track_number, order.userID)) 
    
    res["result"] = None if not res["result"] else Orders(
        ID=res["result"][0],
        accountID=res["result"][1],
        track_number=res["result"][2],
        total_cost=res["result"][3],
        completed=res["result"][4]
    )

    if order.track_number == '':
        res = get_all(order.userID)

    if res["result"] is None:
            res["msg"] = "Not found"
            res["code"] = 400
            res["error"] = True

    return res


def get_all(accountID: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM Orders
                                        WHERE accountID = ?
                                       """,
                             args=(accountID,),
                             many=True)
    
    list_orders = []

    if res["result"]:
        for order in res["result"]:
            list_orders.append(Orders(
                ID=order[0],
                accountID=order[1],
                track_number=order[2],
                total_cost=order[3],
                completed=order[4]
            ))

    res["result"] = None if len(list_orders) == 0 else list_orders

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def complete(orderID: int) -> dict:

    # res = get(order_id=orderID)

    # if res["result"]:
    #     if res["result"].completed == True:
    #         res["msg"] = "Already completed"
    #         res["code"] = 400
    #         res["error"] = True

    #         return res

    res = db_manager.execute(query="""UPDATE Orders
                                       SET completed = TRUE 
                                       WHERE ID = ?
                                       RETURNING ID""",
                              args=(orderID,))
    
    # res["result"] = get(order_id=orderID)["result"]

    res["msg"] = "Completed"

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def delete(orderID: int) -> dict:
    check_order = get(order_id=orderID)["result"]
    
    res = db_manager.execute(query="""DELETE FROM Orders WHERE ID = ? """,
                              args=(orderID,))
    
    if check_order is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res