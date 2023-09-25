from database.db_manager import db_manager

from database.models import ListProducts, ProductUpd, ProductDel

def new(product: ListProducts) -> dict:
    res = db_manager.execute(query="""INSERT INTO ListProducts(orderID, productID, count) 
                                          VALUES(?, ?, ?) 
                                          RETURNING orderID""", 
                              args=(product.orderID, product.productID, product.count))

    res["result"] = None if not res["result"] else get(res["result"][0])

    return res

# def calculate_total_cost(order_id: int) -> int:
#     db_manager.execute(query="""SELECT productID  
#                                     FROM ListProducts 
#                                     WHERE ID = ?""", 
#                               args=(order_id,)) # TODO
    

def get(order_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM ListProducts 
                                       WHERE orderID = ?""", 
                              args=(order_id,)) 
    
    res["result"] = None if not res["result"] else ListProducts(
        id=res["result"][0],
        orderID=res["result"][1],
        productID=res["result"][2],
        count=res["result"][3]
    )

    return res


def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM ListProducts
                                       GROUP BY orderID""", 
                              many=True)

    list_products_lists = []

    if res["result"]:
        for list_products in res["result"]:
            list_products_lists.append(ListProducts(
                id=list_products["result"][0],
                orderID=list_products["result"][1],
                productID=list_products["result"][2],
                count=list_products["result"][3]))
        res["result"] = list_products_lists
    else:
        res["result"] = None

    return res

def update(new_data: ProductUpd) -> dict:
    res = db_manager.execute(query="""UPDATE ListProducts 
                                       SET (productID, count) = (?, ?) 
                                       WHERE (orderID, productID) = (?, ?)
                                       RETURNING orderID""",
                              args=(new_data.new_productID, new_data.count, new_data.orderID, new_data.productID))

    res["result"] = None if not res["result"] else get(res["result"][0])
    
    return res


def delete(data: ProductDel) -> dict:
    return db_manager.execute(query="""DELETE FROM ListProducts WHERE (orderID, productID) = (?, ?) """,
                              args=(data.orderID, data.productID))