from server.database.db_manager import db_manager

from server.database.models import ListProducts, ListProductsUpd, ListProductsDelOrGet
def new(product: ListProducts) -> dict:
    res = db_manager.execute(query="""INSERT INTO ListProducts(orderID, productID, count) 
                                          VALUES(?, ?, ?) 
                                          RETURNING orderID, productID""", 
                              args=(product.orderID, product.productID, product.count))

    res["result"] = None if not res["result"] else getOneProduct(order_id=res["result"][0], product_id=res["result"][1])["result"]

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
                              args=(order_id,),
                              many=True) 
    
    list_products_lists = []

    if res["result"]:
        for list_products in res["result"]:
            list_products_lists.append(ListProducts(
                orderID=list_products[1],
                productID=list_products[2],
                count=list_products[3]))
            
    res["result"] = None if len(list_products_lists) == 0 else list_products_lists

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def getOneProduct(order_id: int, product_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                      FROM ListProducts 
                                      WHERE orderID = ? AND productID = ?""", 
                              args=(order_id, product_id,))
    
    res["result"] = None if not res["result"] else ListProducts(
        orderID=res["result"][1],
        productID=res["result"][2],  
        count=res["result"][3]
    )

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM ListProducts""", 
                              many=True)

    list_products_lists = []

    if res["result"]:
        for list_products in res["result"]:
            list_products_lists.append(ListProducts(
                orderID=list_products[1],
                productID=list_products[2],
                count=list_products[3]))
            
    res["result"] = None if len(list_products_lists) == 0 else list_products_lists

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res

def update(new_data: ListProductsUpd) -> dict:
    res = db_manager.execute(query="""UPDATE ListProducts 
                                       SET (productID, count) = (?, ?) 
                                       WHERE (orderID, productID) = (?, ?)""",
                              args=(new_data.new_productID, new_data.count, new_data.orderID, new_data.productID))

    res["result"] = getOneProduct(order_id=new_data.orderID, product_id=new_data.new_productID)["result"]

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True
    
    return res


def deleteOneProduct(order_id: int, product_id: int) -> dict:
    check_product_in_order = getOneProduct(order_id=order_id, product_id=product_id)["result"]

    res = db_manager.execute(query="""DELETE FROM ListProducts WHERE (orderID, productID) = (?, ?) """,
                              args=(order_id, product_id))
    
    if check_product_in_order is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def delete(order_id: int) -> dict:
    check_order = get(order_id=order_id)["result"]

    res = db_manager.execute(query="""DELETE FROM ListProducts WHERE orderID = ?""",
                              args=(order_id,))

    if check_order is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res