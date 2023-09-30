from server.database.db_manager import db_manager

from server.database.models import RemnantsOfProducts, UpdRemnantsOfProducts

def new(product: RemnantsOfProducts) -> dict:
    res = db_manager.execute(query="""INSERT INTO RemnantsOfProducts(warehouseID, productID, count) 
                                          VALUES(?, ?, ?) 
                                          RETURNING warehouseID""", 
                             args=(product.warehouseID, product.productID, product.count))
    
    res["result"] = None if not res["result"] else getOneProduct(warehouseID=product.warehouseID, productID=product.productID)["result"]
    
    return res


def getOneProduct(warehouse_id: int, productID: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                      FROM RemnantsOfProducts 
                                      WHERE warehouseID = ? AND productID = ?""", 
                              args=(warehouse_id, productID,))
    
    res["result"] = None if not res["result"] else RemnantsOfProducts(
        warehouseID=res["result"][1],
        productID=res["result"][2],  
        count=res["result"][3]
    )

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def get(warehouse_id: int) -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM RemnantsOfProducts 
                                       WHERE warehouseID = ?""", 
                             args=(warehouse_id,),
                             many=True)

    list_warhouses = []

    if res["result"]:
        for warehouse in res["result"]:
            list_warhouses.append(RemnantsOfProducts(
                warehouseID=warehouse[1],
                productID=warehouse[2],
                count=warehouse[3]
            ))
    
    res["result"] = None if len(list_warhouses) == 0 else list_warhouses

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True
        

    return res


def get_all() -> dict:
    res = db_manager.execute(query="""SELECT * 
                                       FROM RemnantsOfProducts""", 
                              many=True)
    
    list_warhouses = []

    if res["result"]:
        for warehouse in res["result"]:
            list_warhouses.append(RemnantsOfProducts(
                warehouseID=warehouse[1],
                productID=warehouse[2],
                count=warehouse[3]
            ))
    
    res["result"] = None if len(list_warhouses) == 0 else list_warhouses

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def update(new_data: UpdRemnantsOfProducts) -> dict:
    res = db_manager.execute(query="""UPDATE RemnantsOfProducts 
                                       SET (productID, count) = (?, ?) 
                                       WHERE (warehouseID, productID) = (?, ?)
                                       RETURNING ID""",
                              args=(new_data.new_productID, new_data.count, new_data.warehouseID, new_data.productID))
    
    res["result"] = None if not res["result"] else getOneProduct(warehouse_id=new_data.warehouseID, productID=new_data.new_productID)["result"]

    if res["result"] is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res


def delete(warehouseID: int, productID: int) -> dict:
    check_product_in_order = getOneProduct(warehouse_id=warehouseID, productID=productID)["result"]
    
    res = db_manager.execute(query="""DELETE FROM RemnantsOfProducts WHERE (warehouseID, productID) = (?, ?) """,
                              args=(warehouseID, productID))
    
    if check_product_in_order is None:
        res["msg"] = "Not found"
        res["code"] = 400
        res["error"] = True

    return res